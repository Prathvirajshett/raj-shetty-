class Employee:
    a=11
class Student(Employee):
    b=12
aa=Student()
print(aa.a)
print(aa.b)
aa=Employee
print(aa.a)
#print(aa.b) will throw error



   