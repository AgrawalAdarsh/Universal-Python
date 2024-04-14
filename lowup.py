a = input("Enter the letter: ")
t = 0
ls1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ls2 = ['A','B','C',"D",'E','F','G','H','I',"J","K",'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in ls1:
	if a == i:
		t = 1
for j in ls2:
	if a == j:
		t = 2
if t == 0:
	print("Please enter a valid entry!")
elif t == 1:
	print("The letter is a lowercase")
elif t == 2:
	print("The letter is a uppercase")
