# Represents a reading plan object. Used for internal data management.
class ReadingPlan:
    # Initializes a new ReadingPlan instance with given attributes.
    def __init__(self, id: int, book_name: str, total_pages: int, target_date: str):
        self.id = id
        self.book_name = book_name
        self.total_pages = total_pages
        self.target_date = target_date

    # Converts the object to a dictionary format for easier JSON serialization
    def to_dict(self):
        return {
            "id": self.id,
            "book_name": self.book_name,
            "total_pages": self.total_pages,
            "target_date": self.target_date,
        }