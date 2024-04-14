# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.  
def numstaking(n):
	ls = []
	flag = 0
	for i in range(n):
		i = int(input("Enter the num:\t"))
		ls.append(i)
	j = set(ls)
	j = list(j)
	return ls[::1] == j[::1]
n = int(input("Enter the no. of entries:\t"))
print("The result is:\t",numstaking(n))
