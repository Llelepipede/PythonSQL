import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
# Replace these values with your actual database connection details
host = 'localhost'
user = 'root'
password = os.getenv('PASSWORD')
database = 'JO'

# Establish a connection to the MySQL server
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Example: Execute a query to fetch data from a table
cursor.execute("SELECT * FROM personne")

# Fetch all the rows
rows = cursor.fetchall()

# Process the fetched data (for example, printing it)
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()