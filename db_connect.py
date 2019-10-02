import pyodbc

# This file will be used to connnect pythin to the database#

# Variables for the connection
server = 'localhost,1433'

database = 'Northwind'

username = 'SA'

password = 'Passw0rd2018'

# Establish a connection

conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

print(conn_nwdb)


# Create a cursor



# Fetch some data

