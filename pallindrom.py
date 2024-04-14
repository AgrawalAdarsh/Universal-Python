n = int(input("Enter the 3 digit number: "))
flag1 = n #let n = 452
rev,temp = 0,0
while(n!=0):
    temp = n%10
    rev=rev*10+temp
    n = n//10
if rev == flag1:
    print("The number is a pallindrome")
else:
    print("Not a pallindrome")
