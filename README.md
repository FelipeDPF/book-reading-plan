# Book Reading Plan

## Description
The **Book Reading Plan** is a web application designed to help users organize their reading habits. Users can input book details, total pages, and a target completion date, and the app calculates the number of pages to read daily.

![Demo](demo/demo.gif)

## Features
- Add books to your reading plan.
- Automatically calculates the number of pages to read per day.
- View all books in a structured table format.
- Delete books from your plan.

## Technologies Used
Refer to the official documentation for installation instructions for the following technologies:
- **Frontend**: Angular 19.1.4
- **Backend**: Python FastAPI
- **Database**: MySQL

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/FelipeDPF/book-reading-plan.git
   cd book-reading-plan``` 

### BACKEND SETUP (FastAPI + MySQL)
2. Navigate to the backend folder:
```cd api```

3. (Optional but recommended) Create and activate a virtual environment:
```python3 -m venv venv```
```source venv/bin/activate```  # For Windows use: venv\Scripts\activate

4. Install backend dependencies:
```pip install -r requirements.txt```

5. Start the backend server:
```python3 -m uvicorn main:app --reload```

### Backend will be live at:
http://127.0.0.1:8000
### Swagger API Docs:
http://127.0.0.1:8000/docs

💡 If you change or install new packages, regenerate `requirements.txt` using:
pip freeze > requirements.txt


### FRONTEND SETUP (Angular)
1. Navigate to the Angular frontend folder:
```cd ul/book-reading-plan```

2. Install frontend dependencies:
```npm install```

3. Run the frontend Angular app:
```ng serve --o```

# Frontend will be live at:
http://localhost:4200


# PROJECT STRUCTURE
```
book-reading-plan/
├── api/                    # FastAPI backend
│   ├── main.py
│   ├── models/
│   ├── routers/
│   ├── services/
│   ├── schemas/
│   └── requirements.txt    # ← Python dependencies
├── ul/book-reading-plan/   # Angular frontend
│   ├── src/
│   ├── package.json        # ← Node dependencies
│   └── ...
└── README.md
```

# NOTES
- Make sure MySQL is installed and running if backend needs it.
- The frontend and backend communicate locally (CORS already enabled in FastAPI).

## Future Improvements
- Add user authentication.
- Implement update functionality for books.
- Enhance UI/UX with more themes and animations.
