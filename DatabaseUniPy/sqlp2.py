import mysql.connector
try:
	con=mysql.connector.connect(user='root',password='Ady@09082004',host='127.0.0.1',database='Univ python')
	cursor=con.cursor()
	while True:
		sname=input("Enter student name:\t")
		sadd=input("Enter student add:\t")
		mob=input("Enter student mob:\t")
		unm=input("Enter username:\t")
		upw=input("Enter password:\t")
		branch=input("Enter the branch of study of student:\t")
		status=int(input("Status :(dead=0 or alive=1)::\t"))
		sql="insert into Student(sname,sadd,mob,unm,upw,branch,status)values('%s','%s','%s','%s','%s','%s',%d)"
		cursor.execute(sql%(sname,sadd,mob,unm,upw,branch,status))
		print("Record inserted successfully")
		option=input("Do you want to insert one more record ?[Yes|No] ??")
		if option=='No':
			con.commit()
			break
except Exception as e:
	if con:
		con.rollback()
		print("There is a problem in sql: ",e)
finally:
	if cursor:
		cursor.close()
	if con:
		con.close()
