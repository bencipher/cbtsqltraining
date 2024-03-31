# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

sql_server = os.getenv("SQL_SERVER")
sql_database = os.getenv("SQL_DATABASE")
sql_username = os.getenv("SQL_USERNAME")
sql_password = os.getenv("SQL_PASSWORD")


def load_db():
    # Connect to SQL Server
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={sql_server};"
        f"DATABASE={sql_database};"
        f"UID={sql_username};"
        f"PWD={sql_password}; "
        f"TrustServerCertificate=yes;"
        # f" Connection Timeout=30; "
        # f"Network=DBMSSOCN"
    )

    cursor = conn.cursor()

    # Insert data into T1
    for i in range(1, 2):
        cursor.execute("INSERT INTO T1 (id) VALUES (?)", i)
    conn.commit()

    # Insert data into T10
    for i in range(1, 11):
        cursor.execute("INSERT INTO T10 (id) VALUES (?)", i)
    conn.commit()

    # Insert data into T100
    for i in range(1, 101):
        cursor.execute("INSERT INTO T100 (id) VALUES (?)", i)
    conn.commit()

    # Insert data into T500
    for i in range(1, 501):
        cursor.execute("INSERT INTO T500 (id) VALUES (?)", i)
    conn.commit()

    # Close connection
    conn.close()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    load_db()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
