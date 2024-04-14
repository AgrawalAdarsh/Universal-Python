s=input("Enter the string: ")
prev=''
ns=''
for x in s:
	if x != prev:
		ns+=x
	prev=x
print("New Corrected string is :\t",ns)
