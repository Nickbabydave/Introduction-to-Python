#Simple BMI Calculator

#Ask the user to enter their weight in kilograms
weight = float(input("Enter your weight in kilograms (kg): "))

#Ask the user to enter their height in metres
height = float(input("Enter your height in metres (m): "))

#Calculate BMI
bmi = weight / (height ** 2)

#Display the result
print(f"Your BMI is: {bmi:.2f}")

## Explanation
##So this Python statement:

##bmi = weight / (height **2)
##means:
## / = division
## ** = exponent/power
##height **2 = height squared
##and:
##primt(f"Your BMI is: {bmi:.2f}")
##uses an f-string, while .2f displays the answer to two decimal places.