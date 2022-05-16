from os import makedirs
from unicodedata import name
class Student:
    def __init__(self,name,marks,center):
        self.name=name
        self.marks=marks
        self.center=center 
    def Studentobj(self):
        print(f"the name is{self.name}")
        print(f"the marks is{self.marks}")
        print(f"the center is {self.center}")
shetty=Student("shetty",52,"bangalore")
arun=Student("arun",50,"udupi")
    
shetty.Studentobj()
arun.Studentobj()

