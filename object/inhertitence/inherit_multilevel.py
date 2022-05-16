class Parent:
    a=10
class Child1(Parent):
    b=20
class Child2(Child1):
    c=30
object = Child2()
print(object.a)
#print(object.b)
#print(object.c)
