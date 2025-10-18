#tuples are like list used to store a sequence of objects but tuples are immutable ie cannot be change/modified once created
#a key differentiator is that lists use [] while tuples use ()

numbers = (1, 2, 3, 4, 5, 5, 6, 7, 8, 9)

num1 = numbers.count(5)#checks how many times an element has been repeated
num2 = numbers.index(5)#return the index of the first occurrence/repetition of the given element

print(num1)
print(num2)