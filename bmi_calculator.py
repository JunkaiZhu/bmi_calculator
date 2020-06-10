while True:
    try:
        h = float(input("Please enter your height in meters: "))
        w = float(input("Please enter your weight in kilograms: "))
        break
    except ValueError:
        print("That was not a number. Please input again")

bmi = (w)/(h*h)

print("Your bmi is: " + str(bmi))
if bmi>25:
    print("You are overweight")
elif bmi<25 and bmi>16:
    print("You are normal weight")
elif bmi<16:
    print("You are underweight")

