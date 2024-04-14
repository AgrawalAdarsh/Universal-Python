n = int(input("Entet the year:\t"))
if n%4==0 and n%100 == 0 and n%400==0:
    print("This is a leap year")
elif n%4 != 0:
    print("This isn't a leap year")
elif n%4 == 0 and n % 100 != 0:
    print("This is a leap year")
elif n%4 == 0 and n % 100 == 0 and n % 400 != 0:
    print("This is  not a leap year")
