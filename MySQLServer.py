import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust host, user, and password as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Tafariblessed@0123'  # Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database (if not exists ensures it won't fail if already present)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error:
        print(f"Error: {Error}")
    finally:
        # Ensure the connection is closed properly
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
