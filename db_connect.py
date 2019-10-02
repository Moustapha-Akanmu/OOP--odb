import pyodbc
#In this file we will make our connection

#parameters / variables for connection
server = 'localhost, 1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

#Establish a connection
conn_northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

print(conn_northwind)

# create a cursor

#Fetch some data

