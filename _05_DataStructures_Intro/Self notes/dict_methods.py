studentdetails={
    "name":"shetty",
    "standard":"12th",
    "fees":5000
}
print(studentdetails)
print(studentdetails['name'])
print(studentdetails['fees'])
print('*****************')
print('length is:',len(studentdetails))
pra="name"in studentdetails
print("pra is:",pra)
print(studentdetails)
print("***************")
print("keys are:",studentdetails.keys())
print("values are:",studentdetails.values())
print("items are:",studentdetails.items())
print("update:",studentdetails.update())
print("get",studentdetails.get('name'))