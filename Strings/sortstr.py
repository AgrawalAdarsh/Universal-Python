s=input("Enter the alphanumeric string: ")
dig=char=output=""
for i in s:
	if i.isalpha():
		char+=i
		#print("char= ",char)
	else:
		dig+=i
		#print("dig= ",dig)
for i in sorted(char):
	output+=i
for i in sorted(dig):
	output+=i
print(output)
