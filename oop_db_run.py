from oop_db_connect import *

server ='localhost, 1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

db_nw = connectMsServer(server, database, username, password)
print(db_nw)
print(db_nw.conn_nwdb)


print(db_nw.sql_query)

print(db_nw)