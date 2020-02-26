def calculate_BMI(height, weight): 
    bmi = weight/(height**2) 
    return bmi

while True:
    try:
        height = float(input("Please enter your height: "))
        break
    except ValueError:
        print("Please enter value in meters, for example 1.60")
        continue

while True:
    try:
        mass = float(input("Please enter your mass: "))
        break
    except ValueError:
        print("The value must be a number.")
        continue

bmi = calculate_BMI(height, mass)
print("Body Mass Index (BMI): {} kg/m^2".format(bmi))
