a=int(input("enter salary:"))
b=int(input("enter year of sevice:"))
if(b>10):
   netbonus=(a*.1)
   print("the net bonus is:",netbonus)
elif(b>=6)and(b<=10):
    netbonus=(a*.08)/100
    print("the net bonus is:",netbonus)
else:
    netbonus=(a*.05)/100
    print("the net bonus is:",netbonus)