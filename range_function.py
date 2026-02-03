#the range function is used to generate a sequence of numbers
numbers = range(11) #the number specified here is the index number not the element i.e it will start from the index of 0(0) up to the index of 11 (10)
#you can also specify the starting and ending numbers ie range (2, 8). NB// the ending number will be excluded
#you can also specify the interval to interate at > range(1, 14, 2) ie the starting number, the ending number, the interval

num = range(2, 8)

num2 = range(1, 15, 2)

for nums in numbers:
    print(nums)

for num1 in num:
    print(num1)

for num0 in num2:
    print(num0)