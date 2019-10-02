from oop_db_connect import *

server = 'localhost,1433'

database = 'Northwind'

username = 'SA'

password = 'Passw0rd2018'

db_nw = ConnectMsS(server, database, username, password)


print(db_nw)

print(db_nw.conn_nwdb)

print(db_nw.cursor.execute("SELECT * FROM Products").fetchone())


print(db_nw.sql_query_fetchone("SELECT * FROM Products"))



print(db_nw.average_price_products())

print(db_nw.list_all_sql_entries("Products"))