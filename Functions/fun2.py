#various arguements and their functions ::::
#1. position arg
def sum_sub(a,b):
	suma=a+b
	suba=a-b
	return suma, suba
sum_sub(10,20)
sum_sub(20,10)

#2. keyword arg
def rand(arg1,arg2):
	print("This is ",arg1,arg2)
	return (arg1+arg2)
rand(arg1=20,arg2=10)
rand(arg2=10,arg1=20)

#3.def arg
def bootup(name='Guest'):
	print("Hello Dear",name,"We MS welcome u here!")
bootup(name="JP")
bootup()
bootup("JP")
bootup("Ady")


