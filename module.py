#a model is like a code drawer, keeps functions and variable organized for reuse
#keep modules focused each should handle one area
#name them clearly
#watch out for name clushes, if 2 module have the same function name use aliases

def say_hi():
    print("hi there")

my_var = 42
def add_num(a, b):
    return a + b

#square a number
def square(num):
    return num * num

#cube a number
def cube(num):
    return num * num * num

# a constant
earth_gravity = 10

#a function to raise a number to a power
def power(base, exp):
    return base ** exp