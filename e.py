a=int(input("Enter a year"))
if(a%400==0 and a%100==0):
    print("Leap year")
elif(a%4==0 and a%100!=0):
    print("Leap year")
else:
    print("Not a leap year")
