import connectDB as db


cx = db.get_connection()

SQL_QUERY = """
                    SELECT TOP (1000) [CustomerID]
                        ,[CompanyName]
                        ,[ContactName]
                        ,[ContactTitle]
                        ,[Address]
                        ,[City]
                        ,[Region]
                        ,[PostalCode]
                        ,[Country]
                        ,[Phone]
                        ,[Fax] 
                    FROM Customers
            """

cursor = cx.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(f"{r.CustomerID}\t{r.Address}\t{r.CompanyName}")

