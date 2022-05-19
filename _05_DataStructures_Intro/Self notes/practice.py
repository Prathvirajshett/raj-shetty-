strng='shetty'
print(len(strng))
print(strng.endswith("ty"))
print(strng.count("t"))
print(strng.capitalize())
print(strng.find("e"))
print(strng.replace('y','t'))
print(strng.encode())
print("***********")

#list method
l1=[1,8,7,2,21,15]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.append(2)
print(l1)
l1.insert(2,3)
print(l1)
l1.pop(2)
print (l1)
l1.remove(2)
print(l1)

#tuple method
a=(1,9,2)
print(a.count(1))
print(a.index(1))

#dict methods
a={"name":"prathvi",
   "from":"india",
   "marks":[92,98,96]}
print(a["name"])
print(a.items())  #list of tuples
print(a.keys())
(a.update({"friend":"ram"}))
print(a)
print(a.get("name"))


#operations on sets
a={1,8,2,3}
# print(len(a))
# (a.remove(8))
# print(a)
# a.pop()
# print(a)
#a.clear()
print(a.union({8,11}))
print(a.intersection({8,11}))
