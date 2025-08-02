from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI()

NOTES_DIR = "notes"


if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

class Note(BaseModel):
    content: str

# POST /notes/ (Add a note)
@app.post("/notes/")
def create_note(title: str, note: Note):
    file_path = os.path.join(NOTES_DIR, f"{title}.txt")
    if os.path.exists(file_path):
        raise HTTPException(status_code=400, detail="Note already exists.")
    try:
        with open(file_path, "w") as f:
            f.write(note.content)
        return {"message": f"Note '{title}' created successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#  GET /notes/{title} (Read a note) 
@app.get("/notes/{title}")
def read_note(title: str):
    file_path = os.path.join(NOTES_DIR, f"{title}.txt")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Note not found.")
    try:
        with open(file_path, "r") as f:
            content = f.read()
        return {"title": title, "content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#POST /notes/{title} (Update a note) 
@app.post("/notes/{title}")
def update_note(title: str, note: Note):
    file_path = os.path.join(NOTES_DIR, f"{title}.txt")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Note not found.")
    try:
        with open(file_path, "w") as f:
            f.write(note.content)
        return {"message": f"Note '{title}' updated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#DELETE /notes/{title} (Delete a note) 
@app.delete("/notes/{title}")
def delete_note(title: str):
    file_path = os.path.join(NOTES_DIR, f"{title}.txt")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Note not found.")
    try:
        os.remove(file_path)
        return {"message": f"Note '{title}' deleted successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
