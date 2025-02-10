from fastapi import APIRouter, Form
from core.database import get_db_cursor  # Import the function to retrieve database connection and cursor

router = APIRouter()  # Create an API router for handling routes related to reading plans

# Fetch all reading plans from the database
@router.get("/get_reading_plans")
def get_reading_plans():
    conn, cursor = get_db_cursor()  # Retrieve database connection and cursor
    query = """
    SELECT 
        id, 
        book_name, 
        total_pages, 
        target_date, 
        FLOOR(total_pages / DATEDIFF(target_date, CURDATE())) AS pages_per_day 
    FROM sys_reading_plan
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()  # Close the database connection to prevent leaks
    return results

@router.post("/add_reading_plan")
def add_reading_plan(book_name: str = Form(...), total_pages: int = Form(...), target_date: str = Form(...)):
    """ Add a new reading plan to the database """
    conn, cursor = get_db_cursor()  # Retrieve database connection and cursor
    query = "INSERT INTO sys_reading_plan (book_name, total_pages, target_date) VALUES (%s, %s, %s)"
    cursor.execute(query, (book_name, total_pages, target_date))
    conn.commit()  # Commit the transaction to save changes
    conn.close()  # Close the connection after execution
    return {"message": "Reading plan added successfully!"}

@router.post("/delete_reading_plan")
def delete_reading_plan(id: int = Form(...)):
    """ Delete a reading plan from the database using its ID """
    conn, cursor = get_db_cursor()  # Retrieve database connection and cursor
    query = "DELETE FROM sys_reading_plan WHERE id = %s"
    cursor.execute(query, (id,))
    conn.commit()  # Commit the transaction
    conn.close()  # Close the connection after execution
    return {"message": "Reading plan deleted successfully!"}