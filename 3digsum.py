#code for sum of 3 digit no.'s digits
n=int(input("N=\t"))
sum=0
temp=n%10
sum+=temp
n=n//10
temp=n%10
sum+=temp
n=n//10
sum+=n
print(sum)
