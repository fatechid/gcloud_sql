# Simple Google Cloud SQL Connection with Python<br />
generate client certificate at **SQL -> Connection -> Create a client Cerfiticate**<br />
And edit this line for your client certificate dir<br />
    'ssl_ca': '/server-ca.pem',<br />
    'ssl_cert': '/client-cert.pem',<br />
    'ssl_key': '/client-key.pem'<br /><br />
This is a pretty big security issue, that's why we use SSL encryption to restrict access to our instance.<br />

Than, edit this line with your instance information<br />

**DB_server = "your_host"**<br />
**DB_username = "your_username"**<br />
**DB_password = "your_password"**<br />

also we can create database for testing when connection is successfully.<br />
**cursor.execute("CREATE DATABASE " + database_input)  #create a new database**<br />
