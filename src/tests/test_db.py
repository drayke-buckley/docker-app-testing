import pyodbc
import pytest

class TestDatabase:
    def test_database(self):
        conn = pyodbc.connect(
        "Driver={ODBC Driver 18 for SQL Server};"
        "Server=database,1433;"
        "Database=test;"
        "UID=SA;"
        "PWD=Password1234!;"
        "TrustServerCertificate=yes;"
        )
        # Create a cursor
        cursor = conn.cursor()

        try:
            # Check if the table exists
            cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'test'")
            table_exists = cursor.fetchone()[0] == 1

            # Check if the column exists
            cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'test' AND COLUMN_NAME = 'test'")
            column_exists = cursor.fetchone()[0] == 1

            # Check if the row exists
            cursor.execute("SELECT COUNT(*) FROM test WHERE test = 'test'")
            row_exists = cursor.fetchone()[0] == 1

            # Assert that all conditions are met
            assert table_exists and column_exists and row_exists
        finally:
            cursor.close()
            conn.close()
