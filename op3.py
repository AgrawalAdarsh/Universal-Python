a=int(input("A="))
b=int(input("B="))
#using '/' gives a floating value answer
#using '//' gives a integer answer only if both the inputs are
#int else  if even 1 is float ans will be float
print("Using '/' for a/b",a/b)
print("Using '//' for a//b",a//b)
print("Now doing again but with a as float and b as int ")
a=float(input("A="))
b=int(input("B="))
print("Using '//' for a//b",a//b)
print("Using '/' for a/b",a/b)
print("Now doing again but with b as float and a as int ")
a=int(input("A="))
b=float(input("B="))
print("Using '//' for a//b",a//b)
print("Using '/' for a/b",a/b)
print("Now doing again but with b as float and a as well float ")
a=float(input("A="))
b=float(input("B="))
print("Using '//' for a//b",a//b)
print("Using '/' for a/b",a/b)