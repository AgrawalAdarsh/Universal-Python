'''The formula for simple interest (I) is:

\[ I = P \times r \times t \]

Where:
- \( I \) is the simple interest,
- \( P \) is the principal amount (the initial amount of money),
- \( r \) is the interest rate (expressed as a decimal),
- \( t \) is the time the money is invested for (in years).

So, to calculate the simple interest, you multiply the principal amount by the interest rate and the time period.'''
p = int(input("Enter the principal amount: "))
r = int(input("Enter the interest rate: "))
t = int(input("Entet the time money is invested for: "))
I = p*r*t/100
print("The Simple Interest is: ",I)
