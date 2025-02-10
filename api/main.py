from fastapi import FastAPI
from routers import plans  # Importing the router module for handling API routes
from fastapi.middleware.cors import CORSMiddleware
from core.database import get_db_cursor  # Importing the database connection function

app = FastAPI()

# Enable CORS to allow cross-origin requests (useful for frontend communication)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include API routes from the plans router
app.include_router(plans.router)

# Initialize the database connection (creates a new connection on startup)
get_db_cursor()

@app.get("/")
def root():
    return {"message": "Welcome to the Book Reading Plan API!"}