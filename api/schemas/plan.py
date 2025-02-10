from pydantic import BaseModel

# Pydantic model for validating incoming request data.
# Ensures that API requests include the correct structure and data types.
class ReadingPlan(BaseModel):
    book_name: str
    total_pages: int
    target_date: str