import mysql.connector
from subprocess import check_output
from datetime import datetime
import os

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'klavs',
    'password': 'klavs321',
    'database': 'python_outputs'
}

# Function to execute a Python file and store its output in the database
def execute_and_store_output(file_name):
    try:
        # Execute the Python file
        output = check_output(['/home', file_name], text=True)

        # Connect to the MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert the output into the database
        insert_query = "INSERT INTO file_outputs (file_name, output) VALUES (%s, %s)"
        data = (file_name, output)
        cursor.execute(insert_query, data)

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        print(f"Output from {file_name} successfully stored in the database.")
    except Exception as e:
        print(f"Error executing {file_name}: {e}")
execute_and_store_output('joki.py')
