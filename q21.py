a = int(input("Enter the 3 dig number: "))
rv = 0
org = a
sm = 0
temp = a % 10
rv = (rv*10)+temp
sm+=temp
a = a // 10
temp = a % 10
rv = (rv*10)+temp
sm+=temp
a = a // 10
temp = a % 10
rv = (rv*10)+temp
sm+=temp
a = a // 10
print("The reverse of the num is: ",rv)
print("The sum of the number is : ",sm)
