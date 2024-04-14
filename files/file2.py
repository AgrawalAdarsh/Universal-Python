fptr = open("randtxt2.txt",'w')
#using write() to write 1 line at a time and writelines() for a list of lines as a entry
n = int(input("Enter the no. of line to input:\t"))
for i in range(1,n+1):
	st1=input("Data=\t")
	fptr.write(st1)
	fptr.write("\n")
print("Data written to the file successfully")
fptr = open("randtxt2.txt",'r')
data = fptr.read()
print("Data in file:\t", data)
fpt.close()		
