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
#Allow us to execute readonly queries on the database
cursor = conn_northwind.cursor()

#using .execute() on cursor
#cursor.execute("SELECT @@version;")

#using .execute() on cursor
cursor.execute("SELECT * FROM Customers;")

#Fetch rows from cursor - fetchione
row = cursor.fetchone()
print(row)


# .fecthall()
 #this is bad practise
 # We don't use this
rows = cursor.execute("SELECT  * FROM Customers").fetchall()
print(rows)
#rows = cursor.fetcall()
print(len(rows))
print(type(rows)) # if this is a list, we can iterate

# Fetch one data using for loop

rows_4 = cursor.execute("SELECT * FROM Products").fetchall()
# we can iterate
for record in rows_4:
    print(type(record))
    print (record.UnitPrice) # We can access the column of a epcific record
    #howerve this is dangerous as we can clog our machine with loads of date
    #hence we can use while Loop to be more efficient
    # not a good practise as there is a limited amount of ram 

rows_5 = cursor.exceute("SELECT * FROM Products")
while True:
    record = rows.fetchone()
    if record is None: # once it reaches the end
        break
    print(record.UnitPrice)



#Fetch some data

