#class,property,method,propert&setter

from symtable import SymbolTableFactory


class Employee:
    def __init__(self,salary,increment) -> None:
        self.salary=salary
        self.increment=increment
    @property
    def salaryAfterIncrement(self):
     return self.salary*(1+self.increment)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self):
     self.salary =self.salry*(1+self.increment)
emp1=Employee(10000,.1)
print(emp1.salaryAfterIncrement)
emp1.salaryAfterIncrement