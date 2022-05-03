#product of digits
number=int(input("enter a number :"))
product=1
while number!=0:
    rem=number%10
    product=product*rem
    number=number//10
print(product)

