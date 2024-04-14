a = input("Enter the character: ")
ls = ['a','e','i','o','u']
t = 0
for i in ls:
	if a == i:
	    	t=1
if t == 1:
	print("The ",a,"is a vowel")
elif t == 0:
	print("The ",a,"is a consonant")
		
