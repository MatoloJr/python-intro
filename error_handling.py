#error handling catches mistakes before they happen thus keeping your program running smoothly

#the try block i.e it runs the code and except catches the error
try:
    result = 10/0
except ZeroDivisionError:
    print("Can't be divided by zero")

#catching invalid input errors
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("That's not a number")

#handling division and input errors together
try:
    num = int(input("Enter 2nd number: "))
    results = 10 / num
except ValueError:
    print("That's not a number")
except ZeroDivisionError:
    print("Can't be divided by zero")
else:
    print(f"Results: {results}")

#run code even if no errors occur
try:
    num = int(input("Enter 3rd number: "))
    results = 10 / num
except ValueError:
    print("That's not a number")
except ZeroDivisionError:
    print("Can't be divided by zero")
else:
    print(f"Results: {results}")
finally:
    print("Done Calculating")

#building a safe calc with error handling
while True:
    try:
        op = input("Enter calculation operation: (+, -, *, /, %): ")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if op == "+":
            resultz = num1 + num2
        elif op == "-":
            resultz = num1 - num2
        elif op == "*":
            resultz = num1 * num2
        elif op == "/":
            resultz = num1 / num2
        elif op == "%":
            resultz = num1 % num2
        else:
            raise ValueError("Invalid operation")
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Can't be divided by zero")
    else:
        print(f"Results: {resultz}")
    finally:
        print("Ready for next calculation")