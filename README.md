# Book Reading Plan

## Description
The **Book Reading Plan** is a web application designed to help users organize their reading habits. Users can input book details, total pages, and a target completion date, and the app calculates the number of pages to read daily.

## Features
- Add books to your reading plan.
- Automatically calculates the number of pages to read per day.
- View all books in a structured table format.
- Delete books from your plan.

## Technologies Used
- **Frontend**: Angular 19.1.4
- **Backend**: Python FastAPI
- **Database**: MySQL

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/FelipeDPF/BookReadingPlan.git
   cd BookReadingPlan``` 

2. Set up the backend:
- Install dependencies:
 ```pip install fastapi mysql-connector-python uvicorn```
- Start the backend server:
```uvicorn main:app --reload```

3.	Set up the frontend:
- Install dependencies:
```npm install```
- Start the Angular app:
```ng serve --o```

4. Access the application in your browser:
```http://localhost:4200```

## Future Improvements
- Add user authentication.
- Implement update functionality for books.
- Enhance UI/UX with more themes and animations.