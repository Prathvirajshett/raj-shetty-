a=int(input("number of days:"))
if(a<=0):
    print("enter valid date")
elif(a<=5):
    perday=2
    charge=perday*a
    print("the library charge is:",charge)
elif(a>=6)and(a<=10):
    perday=3
    charge=perday*a
    print("the library charge is:",charge)
elif(a>=11)and(a<=15):
    perday=4
    charge=perday*a
    print("the library charge is:",charge)
else:
    perday=5
    charge=perday*a
    print("the library charge is:",charge)

    