#Anonymous or lambda function
s = lambda n:n*n
print("The sq of 4 is:",s(4)) 
s = lambda a,b:a+b
print("The sum of 2 & 3 is",s(2,3))
print("The sum of 2 & 3 is",s(3,2))
print("The sum of 2 & 3 is",s(a=2,b=3))
print("The sum of 2 & 3 is",s(b=3,a=2))
s = lambda a,b:a if a>b else b
print("The greater of 10 and 9 is",s(10,9))
