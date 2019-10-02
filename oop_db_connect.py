import pyodbc
import math

#Concept of 'Strong Params' -
# - Avoid SQL injections
# - Never trust user input
# - Filer for SQL injections

class ConnectMsS():

    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)


        self.cursor = self.conn_nwdb.cursor()

    def sql_query(self, s_query):
        return self.__filter_query(s_query)

    def sql_query_fetchone(self, s_query):
        return self.__filter_query(s_query).fetchone()

    def __filter_query(self, s_query): # Filters for bad queries
        return self.cursor.execute(s_query)

    def print_all_products_from_table(self, table):
        query_rows = self.__filter_query(f"SELECT * FROM {table}")
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            print(record)

    def average_price_products(self):
        query_1 = self.__filter_query('SELECT * FROM Products')
        prices = []


        while True:
            #get individual prices and append
            record = query_1.fetchone()
            if record is None:
                break
            prices.append(record.UnitPrice)

            #Divide by length of rows

        return (sum(prices)/len(prices))


        # CRUD

        # Create 1 entry
        # use INSERT

        # Read all entries of one table
        # --- Fetch specific record

    def list_all_sql_entries(self, table):
        query = self.__filter_query(f"SELECT * FROM {table}")

        while True:
            #get individual prices and append
            record = query.fetchone()
            if record is None:
                break
            print(record)




        # Reda one entry
        #--- Fetch a specific record
        #--- Get one value using ID

    def read_one(self, entry):
        query = self.__filter_query("SELECT * FROM Customers")


        while True:
            #get individual prices and append
            record = query.fetchone()
            if record is None:
                break
            elif entry in record:
                return entry ,

            #Divide by length of rows




        # Update one entry
        #--- Get ID of record to update
        #--- Update specific record

        # Destroy / one entry
        # --- Get ID of specific record
        # --- Destroy the specoific record