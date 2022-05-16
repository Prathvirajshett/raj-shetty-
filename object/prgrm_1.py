"""
class Programmer:
 def __init__(self,language,salary,id):
     self.language=language
     self.salary=salary
     self.id=id
 def programmerObj(self):
     print(f"Language is{self.language}")
     print(f"slary is{self.salary}")
     print(f"id is {self.id}")
ajay=Programmer("c++",25000,25)
vijay=Programmer("JAVA",50000,26)
ajay.programmerObj()
vijay.programmerObj()

"""


def isprime(n):
    if n <=1:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True
print(("True") if isprime(12) else print("False"))

