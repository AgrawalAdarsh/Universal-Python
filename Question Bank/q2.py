# Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
ls = []
n = int(input("Enter the range of num in list:\t"))
for i in range(n):
	i = int(input("Enter the num:\t"))
	ls.append(i)
print(ls[2::3])
for i in ls[2::3]:
	ls.remove(i)
print("After removal list is :\t",ls)	
