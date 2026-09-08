#Basic Calculator

#ask the user to enter two numbers
num1 =float(input("Enter the first number: "))
num2 =float(input("Enter the second number: "))

#Ask the user to choose an operation
operation = input("Choose an operation (+, -, *, /): ")

#Perform the selected calculation
if operation == "+":
    result = num1 + num2
    print("Result:", result)

elif operation == "-":
    result = num1 - num2
    print("Result:", result)

elif operation == "*":
    result = num1 * num2
    print("Result:", result)

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid operation.")
