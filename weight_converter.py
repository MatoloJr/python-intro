weight = input("Enter your weight: ")
unit = input("Enter the weight unit (K)g or (L)bs: ")

if unit.upper() == "K":
    converted = float(weight) / 0.45
    print("you weigh: " + str(weight) + " Kg")
elif unit.upper() == "L":
    converted = float(weight) * 0.45
    print("you weigh: " + str(weight) + " Lbs")
else:
    print("Enter a valid unit")
