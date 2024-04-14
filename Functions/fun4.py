#global local var and "gloal" keyword usage:
a=9000
print("Initially:",a)
def demon():
	#print("1:",a)
	global a  #10000
	print("2:",a)
	a = 15000
	print("3:",a)
def demon2():
	print(a)
demon()
demon2()
print("Last:",a)
 
