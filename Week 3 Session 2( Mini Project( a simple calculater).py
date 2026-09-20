# Mini Project
# (Create a function for calculation)

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

def calculate(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    else:
        return"Invalid operator"

result = calculate(number1, number2, operator)
print(result)
