#import the module
import module
module.say_hi()

#importing specific items from the module
from module import add_num, my_var
print(add_num(5, 3))
print(my_var)

#py inbuilt modules
import math
print(math.sqrt(4))
print(math.pi)

#importing specific functions of those module
from math import sin, cos
print(sin(math.pi/2))

#use our custom math functions and the constant
from module import square, cube, earth_gravity, power
print(power(2, 3))
print(square(4))
print(cube(5))
print(earth_gravity)
print(power(2, 3))
