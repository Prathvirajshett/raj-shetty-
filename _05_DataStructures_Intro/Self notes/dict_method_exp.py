#to check key present or not
dic={
    "CAR":"BMW",
    "BIKE":"KTM"
}

#key=input("enetr the key")
if key in dic.keys():
    print("key present and the value is" )
    print(dic[key])
else:
    print("not present")


''''''
LI = [1,2,3]
LIS = [5,7,9]
LI.append(1)
print(LI)
#LI.append(2,3)
LI.append(LIS)
print(LI)
LI.extend(LIS)
print(LI) ''''''