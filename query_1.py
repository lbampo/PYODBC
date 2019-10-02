import pyodbc

# Variables for the connection
server = 'localhost,1433'

database = 'Northwind'

username = 'SA'

password = 'Passw0rd2018'

# Establish a connection

conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

cursor = conn_nwdb.cursor()
print(cursor)

query = cursor.execute("SELECT COUNT(*) Orders FROM Orders").fetchone()

print(query)