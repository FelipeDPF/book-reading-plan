# Book Reading Plan API

## Overview
This directory contains the backend implementation for the Book Reading Plan web application using FastAPI and MySQL. The structure has been modularized to improve maintainability and scalability.

## Updated Backend Structure
```
BookReadingPlan/
│
└── api/
    ├── main.py         # Entry point for the FastAPI application
    ├── core/
    │   ├── database.py  # Database connection and utility functions
    ├── routers/
    │   ├── plans.py     # API routes for managing reading plans
    ├── models/
    │   ├── plan.py      # Data models (if needed for validation)
    ├── schemas/
    │   ├── plan.py      # Request/response schemas
```

## Key Changes
### 1. Modularization
- **Separation of Concerns:** 
  - Moved database connection logic to `core/database.py`
  - Created `routers/plans.py` for API routes
  - Created `models/plan.py` for data models
  - Created `schemas/plan.py` for request/response validation

### 2. Database Connection Handling
- `core/database.py` now contains:
  ```python
  import mysql.connector
  
  def get_db_cursor():
      conn = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="sys_******"
      )
      return conn, conn.cursor(dictionary=True)
  ```
- API functions now retrieve a new connection and cursor for each request and close them properly.

### 3. API Routes (`routers/plans.py`)
- Moved route logic from `main.py` to `routers/plans.py`.
- Uses `get_db_cursor()` to interact with the database.
- Ensures connections are closed after executing queries.

### 4. `models/plan.py`
- Defines a `ReadingPlan` class to represent a reading plan object.

### 5. `schemas/plan.py`
- Defines a Pydantic model for request validation.

## How to Run the API
1. Ensure MySQL is running and the database is correctly set up.
2. Navigate to the `api` directory.
3. Run the API with:
   ```sh
   uvicorn main:app --reload
   ```
4. The API will be available at `http://127.0.0.1:8000`.

## Next Steps
- Implement a service layer (`services/plan_service.py`) to handle business logic.
- Add authentication and authorization mechanisms.
