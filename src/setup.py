import pyodbc

# Connect to the SQL Server
conn = pyodbc.connect(
    'Driver={ODBC Driver 18 for SQL Server};'
    'Server=database,1433;'
    'Database=master;'
    "UID=SA;"
    "PWD=Password1234!;"
    "TrustServerCertificate=yes;"
)
conn.autocommit = True
if conn is not None:
    print("Connected to the database")
# Create a new database
cursor = conn.cursor()
cursor.execute('CREATE DATABASE test')
conn.close()

# Connect to the newly created database
conn = pyodbc.connect(
    'Driver={ODBC Driver 18 for SQL Server};'
    'Server=database,1433;'
    'Database=test;'
    "UID=SA;"
    "PWD=Password1234!;"
    "TrustServerCertificate=yes;"
)

# Create a new table
cursor = conn.cursor()
cursor.execute('CREATE TABLE test (test VARCHAR(255))')
cursor.commit()

# Insert a value into the table
cursor.execute("INSERT INTO test (test) VALUES ('test')")
cursor.commit()

# Close the connection
conn.close()
print("Database created and table inserted with a value")