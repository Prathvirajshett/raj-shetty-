
'''def my_funct(a):

 return lambda a:a*n
double=my_funct(2)

print(double(2))
'''
def my_func(n):
    return lambda a:a*n
double=my_func(2)
triple=my_func(3)
print(double(4))
print(triple(4))
