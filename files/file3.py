import time
#Reading file content 
f = open("randtext.txt",'r')
while(True):
	print("Choose any 1:\n1)read()\n2)readlines()\n3)readline()\n4)read(n)")
	choice=int(input("Enter:\t"))
	if choice==1:
		f.seek(0)
		line1 = f.read()
		print(line1)
	#print("\n")
	elif choice==2:
		sub_choice=int(input("Enter sub_choice if\n1}to read without for\n2)to read using for ?\nEnter:\t"))
		if sub_choice == 1:
			f.seek(0)
			line2 = f.readlines()
			print(line2)
		elif sub_choice == 2:
			f.seek(0)
			line2 = f.readlines()
			for i in line2:
				print(i)
	elif choice==3:
		f.seek(0)
		line3=f.readline()
		print(line3)
	elif choice==4:
		n=int(input("Enter the number of line u want to read :\t"))
		f.seek(0)
		line4=f.read(n)
		print(line4)
	ch=input("do you what to exit ? if yes press Y else press N ?:\t")
	while ch not in ['Y','N','y','n']:
		ch = input("Invalid Input.\ndo you what to exit ? if yes press Y else press N ?:\t")
	if ch == 'Y' or ch == 'y':
		break
	elif ch == 'n' or ch == 'N':
		time.sleep(1)
		print("Continuining...\n")
		time.sleep(5)
f.close()
