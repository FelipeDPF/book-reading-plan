import mysql.connector  # Import MySQL connector for database interaction

# Establishes a connection to the MySQL database and returns a connection and cursor. 
# This function is called whenever a new database query needs to be executed.
def get_db_cursor():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sup@r8174",
        database="sys_bookreadingplandb"
    )
    return conn, conn.cursor(dictionary=True)  # Returns both connection and cursor