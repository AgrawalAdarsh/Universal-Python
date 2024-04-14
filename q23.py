#Travel allowance is taken 10% of basic salary 
# pnf is 7.8% of basic 
#da is 500
#Given gross salary = basic + da + ta
#and net = gs + pf
n = int(input("Enter the basic salary of the user: "))
ta = n * 10 / 100
pf = n * 7.8 / 100
da = 500
print("The gross salary is : ",(n+da+ta))
print("The gross salary is : ",(n+da+ta-pf))
