a=int(input("enter the marked price:"))
if (a<=0):
    print("enter valid amount")
if(a>10000):
   discount=.2
   netamount=a-(a*discount)
   print("the net amount is:",netamount)

if(a>7000)and(a>=10000):
    discount=.15
    netamount=a-(a*discount)
    print("the net amount is:",netamount)

if(a<=7000):
    discount=.1
    netamount=a-(a*discount)
    print("the net amount is:",netamount)
