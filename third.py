a=100
b=200
c=100
d=100
print("a",a)
print("b=",b)
print('c=',c)
print("d ",d)
#id() is used to print the address of a object in python
print("a ki id ",id(a))
print("b ki id ",id(b))
print("c ki id ",id(c))
print("d ki id ",id(d))
#Python follows the rule of immutability
#i.e. even if one were to remove or change the value of one it won't affect others
a=400
print("After changing a=400 now ")
print("a",a)
print("b=",b)
print('c=',c)
print("d ",d)
#id() is used to print the address of a object in python
print("a ki id ",id(a))
print("b ki id ",id(b))
print("c ki id ",id(c))
print("d ki id ",id(d))
