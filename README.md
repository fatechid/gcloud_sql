# Simple Gcloud SQL Connection with Python<br />

This is a pretty big security issue<br />
That's why we use SSL encryption to restrict access to our instance.<br />

edit this line with your instance<br />

**DB_server = "your_host"**<br />
**DB_username = "your_username"**<br />
**DB_password = "your_password"**<br />

also we can create database when connection is successfully.<br />
**database_input = input("Enter your database name: ") #database name**<br />
**cursor.execute("CREATE DATABASE " + database_input)  #create a new database**<br />
