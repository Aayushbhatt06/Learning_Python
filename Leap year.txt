y=int(input("Enter the year = "))
if (y%4==0 and y%100!=0) or y%400==0:
    print("its a leap year")
else:
    print("its not a leap year")
