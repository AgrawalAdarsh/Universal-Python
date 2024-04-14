# Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies. 
strin = input("Enter the string:\t")
ls = strin.split(" ")
lsr = []
for i in ls:
	print("The count of {} is {}".format(i,ls.count(i)))
	for j in ls:
		if j in ls:
			ls.remove(j)
	
