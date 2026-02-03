#if statements are used to make decisions

temp = 35

if temp > 30 :
    print("it's a hot day")#the double quotes are used because there is a single quote which acts as the aprostrophy
    print("Have a cold drink")
elif temp > 20 :
    print("It's a nice day")
    print("Have a room temperature drink")
elif temp > 10 :
    print("It's a chilly day")
    print("Have a warm drink")
else:
    print("it's a cold day")
    print("Have a hot drink")