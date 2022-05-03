lst=[]
a=int(input("enter no of subject:"))
for i in range(0,a):
    marks=int(input())
    lst.append(marks)
print(lst)

def average(lst):
    return sum(lst)/len(lst)
avg=average(lst)
print("the avg of all subject is:",avg)
count=0
rep=0
for i in range(len(lst)):
    if (lst[i])>95:
        count=count+1
        if count>=3 and (avg>=65):
          print("gold medal")
for i in range(len(lst)):
    if(lst[i])<65:
        rep=rep+1
    if(rep>=3):
        print("fail")
    elif (avg>=75)and(avg<=90)and(rep<=3):
             print("average performance")
    elif (avg>90):
         print("good performance")
    elif(avg>=65)and(avg<75)and(rep>=3):
         print("give a chance")
    else:
        print("fail")

    


#if (avg>=75)and(avg<=90):
    #print("average performance")
#if(avg>90):
    #
    # print("good performance")


