#this function is used when we need to pass multiple arg and that's stored in a tuple
def narg(*n):
	sm=0
	print(type(n))
	for i in n:
		sm+=i
	print("Sum=\t",sm)
narg()
narg(10)
narg(10,20,30)
narg(10,20,3,0,1,0)
narg(10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,190,180,200)
#this *n as a arguement is called wildcard in term of dos used to store multiple values

