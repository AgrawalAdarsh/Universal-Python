ls = [10,20,30,40,50,60,"Helloo","Vijay",44.525,2+5j]
print("Origional list : ",ls)
print(ls[::-1])#reverses the list
print(ls[::])#gives the list in same order
print(ls[::-3])
"""This ls[_:_:_] is just like seq(from=_,to=_,by=_) of Rlanguage the 1st _ is the
start and 2nd _ is end and 3rd _ is the flow/sequence jumps """
print(ls[::-2])#for example this gives the list in reverse order from the last by 2 space jump
#o/p is 2+5j,Vijay,60,40,20

