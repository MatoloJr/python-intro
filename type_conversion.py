#in py there are 3 types of data; numbers, strings and booleans
#type conversion is used to convert the value of a variable from one type to another

birth_year = input("Enter your birth year: ")#whenever the input function is called it will always return a value as a string by default
age = 2025 - int(birth_year) #add the int function converts the birth_year string value to integer (int)

print(age)

#float() > is used for converting a value to a floating point number > a decimal point number
#bool() > for converting a value to a boolean
#str() > for  converting a value to a string