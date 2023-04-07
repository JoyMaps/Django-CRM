import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'joyline'

	) 
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE jozmcreations")

print("All done!")