import mysql.connector  # Import MySQL connector for database interaction
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Establishes a connection to the MySQL database and returns a connection and cursor. 
# This function is called whenever a new database query needs to be executed.
def get_db_cursor():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return conn, conn.cursor(dictionary=True)  # Returns both connection and cursor