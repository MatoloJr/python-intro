#strings represent any data in textual form
#it is initiated by using either double or single quotes
#a string is technically an object as it has a ton of capabilities

course = 'Python Introduction'

#string capabilities/methods is initiated by typing the variable followed by a period/full stop
#when a function is part of an object it is reffered to as a method
print(course.upper())#used to convert a string to uppercase. This method return a new string not the original
print(course)
print(course.lower())
print('Python' in course)
print(course.find('y'))
print(course.replace('for', '4'))

#other methods include;
#strings are immutable thus these method return a new string not the original
#course.lower() > to convert a string to lowercase
#Also writing print('Python' in course) does the same thing as the find method though it will return a boolean value instead of the index
#course.find('y') > to see if our string value contains a character ('y') or a sequence of characters ('for') and return their index(es)
#course.replace('for', '4') > used to replace something ('for') in a string with something ('4') else
