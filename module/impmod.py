import calci as c
print(c.x)
a = int(input("Enter 1st num: "))
b = int(input("Enter 2nd num: "))
c.sum(a,b)
c.sub(a,b)
c.mul(a,b)
c.div(a,b)
c.floordiv(a,b)

#Using Lambda expression now ::::
n = int(input("Enter the 3rd number for lambda exp: "))
m = int(input("Enter the 4th  number for lambda exp: "))
s = lambda n:n**2
print("The square of n is :",s(n))
l = lambda n:n**0.5
print("The square root of n is: ",l(n))
p = lambda n,m:n if n>m else m
print("The greatest of 3rd and 4th num is :",p(n,m))

