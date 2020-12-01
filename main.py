import mysql.connector
from mysql.connector import errorcode
from mysql.connector.constants import ClientFlag

DB_server = "your_host"
DB_username = "your_username"
DB_password = "your_password"

config = {
    'user': DB_username,
    'password': DB_password,
    'host': DB_server,
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': /server-ca.pem',
    'ssl_cert': '/client-cert.pem',
    'ssl_key': '/client-key.pem'
}

# now we establish our connection
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()  #initialize connection cursor

if cursor:
	print("SQL Connected")
	print()
else:
	print("Something wrong and I can feel it.")

create_db = input("Wanna create database? (Y/n) : ")
if create_db == "y" or "Y":
	try:
		database_input = input("Enter your database name: ") #database name must without space or special char, create with your own code or can handle with Exception :)
		cursor.execute("CREATE DATABASE " + database_input) #create a new database
		cnxn.close()  #close connection
		print("Database created successfully")
		print()
		print("Connection closed.")
	except mysql.connector.Error as err:
		print("DatabaseError",  err.msg)
		print()
		print("Connection closed.") #close connection

else:
	cnxn.close()  # close connection
	print("Connection closed.")
