class Parent1:
    a=10
class Parent2:
    b=20
class Child(Parent1,Parent2):
    c=30
object=Child()
print(object.a)
print(object.b)
print(object.c)
