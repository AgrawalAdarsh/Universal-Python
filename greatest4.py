a = int(input("Enter the 1st number"))
b = int(input("Enter the 2nd number"))
c = int(input("Enter the 3rd number"))
d = int(input("Enter the 4th number"))
if a>b and a>c and a>d:
	print(a,"is the greatest")
elif b>c and b>d:
	print(b,"is the greatest")
elif c>d:
	print(c,"is the greatest")
else:
	print(d,"is the greatest")
