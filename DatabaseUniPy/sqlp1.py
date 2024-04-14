import mysql.connector 
try:
	con=mysql.connector.connect(user='root',password='Ady@09082004',host='127.0.0.1',database='Univ python')
	cursor=con.cursor()
	cursor.execute("insert into Student(sname,sadd,mob,unm,upw,branch,status)values('sanjay Datta','indore','9876543210','sanju','12345','IT',0)")
	con.commit()
	print("Record Inserted Successfully")
except Exception as e:
	if con:
		con.rollback()
		print("There is  a problem with sql ",e)
finally:
	if cursor:
		cursor.close()
	if con:
		con.close()
