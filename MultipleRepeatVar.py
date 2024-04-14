s=input("Enter the string: ")
opt=""
temp=""
for x in s:
	if x.isalpha():
		opt=opt+x
		prv=x
		temp=""
	else:
		temp+=x
		opt=opt+prv*(int(temp)-1)
		"""#Why temp='' not work here ??
		#IT reset before concatenating the 2 digit i.e. if temp=1 then reset then temp=2 no diff with the x before temp."""
print(opt)
#s=a12b14c3
