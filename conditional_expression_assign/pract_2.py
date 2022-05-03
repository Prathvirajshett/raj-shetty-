a=int(input("enter the percentage:"))
if(a>=80):
    print("A+")
elif(a>=60) and (a<80):
    print("A")
elif(a>=50)and(a<60):
    print("B+")
elif(a>=45)and(a<50):
    print("B")
elif(a>=25)and(a<45):
    print("c")
else:
    print("D")