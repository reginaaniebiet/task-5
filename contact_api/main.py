from fastapi import FastAPI, HTTPException, Query, Path
from pydantic import BaseModel, EmailStr

app = FastAPI()

# In-memory contact store
contacts_db = {}

# Contact model
class Contact(BaseModel):
    name: str
    phone: str
    email: EmailStr


# ============ POST: Add a Contact ============
@app.post("/contacts/")
def add_contact(contact: Contact):
    if contact.name in contacts_db:
        raise HTTPException(status_code=400, detail="Contact already exists.")
    
    contacts_db[contact.name] = contact.dict()
    return {"message": "Contact added successfully", "data": contact}


# ============ GET: Search Contact by Name (Query Parameter) ============
@app.get("/contacts/")
def get_contact_by_query(name: str = Query(..., description="Name to search")):
    contact = contacts_db.get(name)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found.")
    return contact


# ============ POST: Update Phone (Path Parameter) ============
@app.post("/contacts/{name}/update-phone")
def update_phone(
    name: str = Path(..., description="Contact name"),
    phone: str = Query(..., description="New phone number")
):
    if name not in contacts_db:
        raise HTTPException(status_code=404, detail="Contact not found.")

    contacts_db[name]["phone"] = phone
    return {"message": "Phone updated", "data": contacts_db[name]}


# ============ POST: Update Email (Path Parameter) ============
@app.post("/contacts/{name}/update-email")
def update_email(
    name: str = Path(..., description="Contact name"),
    email: EmailStr = Query(..., description="New email address")
):
    if name not in contacts_db:
        raise HTTPException(status_code=404, detail="Contact not found.")

    contacts_db[name]["email"] = email
    return {"message": "Email updated", "data": contacts_db[name]}
