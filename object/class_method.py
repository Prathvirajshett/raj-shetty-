class Employee:
    a=10
    b=20
    c=30
    @classmethod
    def setAttrs(cls,a,b,c):
        cls.a=a
        cls.b=b
        cls.c=c
aaa=Employee()
print(Employee.a)
print(Employee.b)
print(Employee.c)
aaa.setAttrs(1,2,3)
print(Employee.a)
print(Employee.b)
print(Employee.c)

