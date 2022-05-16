class Employee:
    a=10
    b=20
    c=30
    @classmethod
    def setAttrs(cls,a,b,c):
        cls.a=a
        cls.b=b
        cls.c=c
    @property
    def length(self):
        return self.a
    @length.setter
    def length(self,value):
        self.a=value
aaa=Employee()

aaa.setAttrs(1,2,3)
print(aaa.length)
aaa.length=50
print(aaa.length)
