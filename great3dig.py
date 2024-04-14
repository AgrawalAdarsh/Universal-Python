n = int(input("Enter the 3 digit number: "))
let = n%10 #n = 456
while(n != 0):
    temp = n%10
    if temp > let:
        let = temp
    else:
        pass
    n = n//10    
print(let,"is the greatest digit")
