from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from file_handler import load_applications, save_applications

app = FastAPI()

class JobApplication(BaseModel):
    name: str
    company: str
    position: str
    status: str  # e.g., "pending", "accepted", "rejected"

@app.post("/applications/")
def add_application(app_data: JobApplication):
    try:
        applications = load_applications()
        applications.append(app_data.dict())
        save_applications(applications)
        return {"message": "Application added successfully", "data": app_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding application: {str(e)}")

@app.get("/applications/")
def get_all_applications():
    try:
        applications = load_applications()
        return applications
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading applications: {str(e)}")

@app.get("/applications/search")
def search_by_status(status: str = Query(..., description="Application status to filter by")):
    try:
        applications = load_applications()
        filtered = [app for app in applications if app["status"].lower() == status.lower()]
        return filtered
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")
