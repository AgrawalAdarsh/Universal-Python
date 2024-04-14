import mysql.connector

connector = mysql.connector.connect(host='localhost', user='root', password='Ady@09082004', database='Univ python')

if connector.is_connected():
	print("Connected successfully")
else:
	print("Failed Connection")

connector.close()
