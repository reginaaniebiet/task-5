# 🚀 FastAPI Project Collection – All Tasks in One Repo

This repo contains 5 FastAPI mini projects. Each project is inside its own folder. You'll learn how to build REST APIs with file handling, query/path parameters, and simple data models.

---

## 📦 Requirements (Run Once)

Install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

---

## 📁 Project Structure

```
fastapi-projects/
│
├── task1-student-result-api/
│   ├── main.py
│   └── students.json
│
├── task2-shopping-api/
│   ├── main.py
│   ├── cart.py
│   ├── product.json
│   └── cart.json
│
├── task3-job-tracker-api/
│   ├── main.py
│   ├── file_handler.py
│   └── applications.json
│
├── task4-notes-api/
│   ├── main.py
│   └── notes/
│       ├── shopping-list.txt
│       └── homework.txt
│
└── task5-contact-api/
    └── main.py
```

---

## 🚀 Running a Project

```bash
cd folder_name  # e.g., task1-student-result-api
uvicorn main:app --reload
```

Then open this in your browser:

```
http://127.0.0.1:8000/docs
```

---

## ✅ Task Descriptions

### 🧮 Task 1: Student Result API

- Add students with subject scores
- Automatically calculate average and grade  
- JSON file: `students.json`

**Endpoints**:
- `POST /students/` → Add student
- `GET /students/{name}` → Get one
- `GET /students/` → All students

---

### 🛍 Task 2: Shopping API with Cart

- View products and add to cart
- Checkout with total calculation  
- JSON files: `product.json`, `cart.json`

**Endpoints**:
- `GET /products/` → List product
- `POST /cart/add?product_id=1&qty=2` → Add to cart
- `GET /cart/checkout` → Total cost

---

### 💼 Task 3: Job Application Tracker

- Add job application
- Search by `status`  
- JSON file: `applications.json`

**Endpoints**:
- `POST /applications/` → Add new
- `GET /applications/` → View all
- `GET /applications/search?status=pending` → Filter

---

### 📝 Task 4: Notes App (File System)

- Create and manage notes
- Stored as `.txt` files in `notes/` folder

**Endpoints**:
- `POST /notes/` → Create note
- `GET /notes/{title}` → Read note
- `DELETE /notes/{title}` → Delete note

---

### 📇 Task 5: Contact API

- Add/search/update/delete contacts  
- Uses dictionary (no JSON file)

**Endpoints**:
- `POST /contacts/` → Add contact
- `GET /contacts/?name=John` → Search
- `PUT /contacts/{name}` → Update
- `DELETE /contacts/{name}` → Delete

---

## 🌍 Test with Swagger

Go to:

```
http://127.0.0.1:8000/docs
```

You’ll see an interactive API tester.

---

## 📤 GitHub Submission (Important)

### ✅ Follow these steps:

```bash
# Step 1: Initialize repo
git init

# Step 2: Track files
git add .

# Step 3: Make first commit
git commit -m "Initial commit"

# Step 4: Add GitHub repo
git branch -M main
git remote add origin https://github.com/your-username/fastapi-projects.git

# Step 5: Push to GitHub
git push -u origin main
```

☑️ Ensure:
- At least 3 commits (`git commit -m "..."`)
- Each task has its own folder
- Repo is **public** and **well structured**

---

## 🧠 Summary

This repo covers:
- API building with FastAPI
- File-based and JSON data handling
- Modular code and clean endpoint design

Test all endpoints via `/docs` and submit your GitHub link.