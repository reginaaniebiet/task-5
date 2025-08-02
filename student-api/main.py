from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

DATA_FILE = "students.json"

#Data Model 
class Student(BaseModel):
    name: str
    subject_scores: dict  # Example: {"Math": 80, "English": 90}
    average: float = 0
    grade: str = ""

#Helper Functions
def load_students():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)

def calculate_average_and_grade(scores: dict):
    if not scores:
        return 0, "N/A"
    total = sum(scores.values())
    average = total / len(scores)
    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"
    return average, grade

#  API Endpoints 
@app.post("/students/")
def add_student(student: Student):
    try:
        students = load_students()

        if student.name in students:
            raise HTTPException(status_code=400, detail="Student already exists.")

        average, grade = calculate_average_and_grade(student.subject_scores)
        student.average = average
        student.grade = grade

        students[student.name] = student.dict()
        save_students(students)

        return {"message": "Student added successfully", "data": student}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/students/{name}")
def get_student(name: str):
    try:
        students = load_students()
        if name not in students:
            raise HTTPException(status_code=404, detail="Student not found.")
        return students[name]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/students/")
def get_all_students():
    try:
        students = load_students()
        return list(students.values())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
