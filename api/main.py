from fastapi import FastAPI, Form
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sup@r8174",
    database="sys_bookreadingplandb"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the Book Reading Plan API"}

# Get all reading plans
@app.get("/get_reading_plans")
def get_reading_plans():
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT 
        id, 
        book_name, 
        total_pages, 
        target_date, 
        FLOOR(total_pages / DATEDIFF(target_date, CURDATE())) AS pages_per_day, 
        created_at 
    FROM sys_reading_plan
    """
    cursor.execute(query)
    results = cursor.fetchall()
    return results

# Add a new reading plan
@app.post("/add_reading_plan")
def add_reading_plan(book_name: str = Form(...), total_pages: int = Form(...), target_date: str = Form(...)):
    cursor = conn.cursor()
    query = """
    INSERT INTO sys_reading_plan (book_name, total_pages, target_date)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (book_name, total_pages, target_date))
    conn.commit()
    return {"message": "Reading plan added successfully!"}

# Delete a reading plan
@app.post("/delete_reading_plan")
def delete_reading_plan(id: int = Form(...)):
    cursor = conn.cursor()
    query = "DELETE FROM sys_reading_plan WHERE id = %s"
    cursor.execute(query, (id,))
    conn.commit()
    return {"message": "Reading plan deleted successfully!"}