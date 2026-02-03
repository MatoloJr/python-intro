#a functions enables you to write it once and use it anytime
# a function is defined by the keyword > def

def say_hello():
    print("Hello and welcome to earth")

#to use/output the function you have to call it

say_hello()
#a function with variables

#name = input("Your name kindly: ")
#
#def your_name(name):
#    print(name)
#your_name(name)#calling the function to output


def your_name(name):
    name = input("Enter your name: ")
    print("hello "+ name)

your_name("")

def add_num(num1, num2):
    return num1 + num2

result = add_num(200, 789)
print("the results are: " + str(result))#

def get_details():
    return 25, ("Bali")
age, city = get_details()
print("Age: " + str(age))
print("City: " + str(city))

operation = input("Enter calculation operation: (+, -, *, /, %)")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

def calc(num1, num2, operation):
    if operation == "+":
        return int(num1) + int(num2)
    elif operation == "-":
        return int(num1) - int(num2)
    elif operation == "*":
        return int(num1) * int(num2)
    elif operation == "/":
        return int(num1) / int(num2)
    elif operation == "%":
        return int(num1) % int(num2)
    else:
        print("Enter a valid operation or number")

calc(num1, num2, operation)