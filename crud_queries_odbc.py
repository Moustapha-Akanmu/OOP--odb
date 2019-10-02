from db_connect import *


# Create 1 entry
# use Insert
# the cursor cannot make transaction (go to documentation to check)

    def create_one_entry(self):

    INSERT INTO northwind.Database_Name.Customer(CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax)\

    VALUES

    ('ANTOM', 'Alfred Futterkiste2', 'Moustapha Akanmu', 'Owner', 'avda. de la Cpontitution','Berlin', '  ','12209','Germany', '0300074321', '030-0076545')


# Read all entries
# fetch all record and return as a list of Dictionaries

# Read 1 entry
# fetch a specific record
# Get one value using IL
# Intake a value to search


# Update 1 entry
# the id of the record to update
# update the specific record
# the Cursor cannot make transaction(go to docuemntation

# Destroy / one entry
# the id of the speciifc record
# destroy the record
# the cursor cannot mae transaction