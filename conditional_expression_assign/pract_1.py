a=int(input("enter total no of working days:"))
b=int(input("enter total no of days for absent:"))
percentage=((a-b)/a)*100
print("the percentage of class attended:",percentage)
if(percentage<75):
    print("student will not be able to sit in exam")