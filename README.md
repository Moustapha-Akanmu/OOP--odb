#Connecting SQL to Python using pyodbc

This is an example of us connecting to our sql server using Python and pyodbc

we will look into:
- Cursor
- Rows
- Querying the db
- Using While Loops for efficient data queries
- Transactions

##connection
Open Database Connectivity (ODBC) 
it helps exstablsing a connection between Python and SQL server so that one can manage data.
it is usually in the form of :
server = '.........'
database = '.......'
username = '.....'
password = '......'


conn_nw = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

##.cursor()

it represent a database cursor. 
usually written as 

cursor = <database_name>.cursor()

##.cursor().execute()


##.