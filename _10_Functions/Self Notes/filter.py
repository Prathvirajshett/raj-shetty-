a=[0,1,2,3]
res=filter(lambda x:x%2==0,a)
print(list(res))
res=(lambda x:x%2!=0,a)
print(list(res))
#it filters the given sequence with help of function that test each element in sequence to be true or not



# res=filter(lambda x:x % 2 ==0,a)  #even no's
# print(list(res))
# res=filter(lambda x: x%2 !=0,a) #odd no's
# print(list(res))