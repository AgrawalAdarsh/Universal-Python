s=input("Enter your string : ")
lst=s.split()
t1=[]
i=0
while i<len(lst):
	t1.append(lst[i][::-1])
	i+=1
opt=" ".join(t1)
print(opt)
