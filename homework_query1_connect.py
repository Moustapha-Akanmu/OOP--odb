import pyodbc

server ='localhost, 1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

conn_nw = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

#How many orders in NWDB?
cursor = conn_nw.cursor()

query_1 = cursor.execute("SELECT COUNT(*) FROM Orders").fetchall()

print(query_1)