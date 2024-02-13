from fastapi import FastAPI
import pandas as pd
import pyodbc

app = FastAPI()

@app.get("/data")
def get_data():
    # Connect to the MS SQL database using SQL authentication
    conn = pyodbc.connect(
        "Driver={ODBC Driver 18 for SQL Server};"
        "Server=database,1433;"
        "Database=test;"
        "UID=SA;"
        "PWD=Password1234!;"
        "TrustServerCertificate=yes;"
    )

    # Execute a query to fetch data from the "test" table
    query = "SELECT * FROM test"
    df = pd.read_sql(query, conn)

    # Close the database connection
    conn.close()
    return df["test"][0]