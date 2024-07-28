import pyodbc

DRIVER = 'ODBC Driver 17 for SQL Server'
SERVER = 'localhost'
DATABASE = 'Northwind'
USERNAME = 'sa'
PASSWORD = 'myPassw@rd'


def get_connection():
    conn_str = (f"""DRIVER={DRIVER};
                    SERVER={SERVER};
                  DATABASE={DATABASE};
                       UID={USERNAME};
                       PWD={PASSWORD}"""
    )
    return pyodbc.connect(conn_str)
