n=int(input("enter a number:"))
if n>1:
    for i in range(2,n):
        if(n%i)==0:
            print("number not a prime number")
            
        else:
            print("is a prime number")
else:
    print("not a prime number")
