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
    # A cursor allows us to execute read only queries on the database

cursor = conn_nwdb.cursor()

# Fetch row from cursor

## /.fetchone
# row = cursor.fetchone()
# print(row)

# .fetchall - This is bad practice. Do not use this

row_2 = cursor.execute("SELECT * FROM Customers;").fetchall()
#print(row_2)
print(len(row_2))

# Using .execute() on cursor
cursor.execute("SELECT @@version;")

cursor.execute("SELECT * FROM Customers;")








# Fetch some data
#
# row_3 = cursor.execute("SELECT * FROM Products").fetchall()
#
# for records in row_3:
#     print(type(records))
#     print(records.UnitPrice) # Accessing the column of a specific record
#                             # This is dangeorus as we can clog our machine with tooo much data (there is a limited amount of RAM
#                             # We can therefore us a while loop to be more efficient
#
row_4 = cursor.execute("SELECT * FROM Products ")

while True: # More efficient way if doing things
    records = row_4.fetchone()
    if records is None:
        break

    print(records.UnitPrice)


