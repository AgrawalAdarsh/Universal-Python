def cal_small(a,b):
	sm=a+b
	sb=a-b
	m=a*b
	d=a//b
	exp=a**b
	return sm,sb,m,d,exp
x=int(input("Enter value 1:"))
y=int(input("Enter value 2:"))
res=cal_small(x,y)
for i in res:
	print("Ans:(sum,sub,mul,div,exp):",i)
