import math
class Calculator:
    
    def __init__(self,number):
     self.number=number
    def square(self):
      return self.number*self.number
    def cube(self):
      return self.number*self.number*self.number
    def sqrt(self):
       return math.sqrt(self.number)
    @staticmethod
    def greet():
       print("good morning")
      
two= Calculator(4)
print(two.square())
print(two.cube())
print(two.sqrt())
#Calculator.greet()
two.greet