#if the no of arguments is unknown,add * before the parameters
def my_funct(*bike):
    print("the top selling bike is",bike[2])

my_funct("bajaj","hero","enfield")



#Arbitrary keyword Arguments, **kwargs
#if you dont knwhow many keyword args that will be passed into your function,add ** before parameter
def my_func(**cars):
    print("my car is",cars["type2"])
my_func(type1="bmw",type2="audi",type3="mustang")