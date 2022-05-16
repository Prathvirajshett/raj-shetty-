class Parent:
    a=10
    def __init__(self) -> None:
        print("parent")
class Child1(Parent):
    b=10
    def _init__(self):
        #super().__init__()
        print("child1")
class Child2(Child1):
    c=10
    def __init__(self) -> None:
        super()._init__() #used to call above constructor
        print("child2")
pp=Child2()
print(pp.a)
print(pp.b)
print(pp.c)

