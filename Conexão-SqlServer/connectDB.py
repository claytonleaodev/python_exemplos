import pyodbc

SERVER = 'localhost'
DATABASE = 'Northwind'
USERNAME = 'sa'
PASSWORD = 'myPassw@rd'


def get_connection():
    conn_str = ("DRIVER={ODBC Driver 17 for SQL Server};"
                 "SERVER= localhost;"
                 "DATABASE=Northwind;"
                 "UID=sa;"
                 "PWD=myPassw@rd"
    )
    return pyodbc.connect(conn_str)
