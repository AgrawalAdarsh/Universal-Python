n=int(input("Enter the 3 digit number: "))
arm=0
flag=n
while(n!=0):
    temp=n%10
    arm+=temp**3
    n=n//10
if flag == arm:
    print("The number is a armstrong")
else:
    print("The number is not a armstorng")
