import pyodbc
#search the concept of 'strong Params'
    #never Ever trust user input
    #Avoid SQL injections
    #Filter for SQL injections

class connectMsServer():

    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.conn_nwdb.cursor()

#
# server ='localhost, 1433'
# database = 'Northwind'
# username = 'SA'
# password = 'Passw0rd2018'
#
# db_nw = connectMsServer(server, database, username, password)
# print(db_nw)
# print(db_nw.conn_nwdb)
#

    def __filter_query(self, query):
        #Doing some filtering for bad querie
        return self.cursor.execute(query)


    def sql_query(self, query):
        return self.__filter_query(query)

    def sql_query_fetchone(self, query):
        return self.__filter_query(query).fetchone

    #we use print instead of return otherwise it will only go to the first rewcord and EXIT
    #only way to use return would have been to put into a dictionnary
    def print_all_product_records(self):
        query_rows = self.__filter_query('SELECT * FROM Products')
        while True:
            record = query_rows.fectchone()
            if record is None:
                break
            print(record)

    def print_all_product_records_from_table(self, table):
        query_rows = self.__filter_query('SELECT * FROM {table}')
        while True:
            record = query_rows.fectchone()
            if record is None:
                break
            print(record)

    def average_price_products(self):
        #query
        query = self.__filter_query('SELECT * FROM Products')
        #Sum all the unit prices
        prices = []
        while True:
            #get individual priced and append to the list
            record = query.fetchone()
            if record is None:
                break
            prices.append(record.UnitPrice)

        # devide by length of rows
        return (sum(prices)/len(prices))

        # query_avg = self.__filter_query('SELECT AVG(UnitPrice) FROM Products')
        # while True:
        #     record = query_avg.fetchone()
        #     if record is None:
        #         break
        #     print(record)



    #CRUD

    #Create 1 entry
        #use Insert
        # the cursor cannot make transaction (go to documentation to check)

    # Read all entries
        #fetch all record and return as a list of Dictionaries

    # Read 1 entry
        #fetch a specific record
        # Get one value using IL
        #Intake a value to search


    # Update 1 entry
        # the id of the record to update
        #update the specific record
            #the Cursor cannot make transaction(go to docuemntation

    # Destroy / one entry
        #the id of the speciifc record
        #destroy the record
            #the cursor cannot mae transaction