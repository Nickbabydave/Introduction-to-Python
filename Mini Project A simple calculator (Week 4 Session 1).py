# Mini Project

try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    result = number1 / number2
    print(result)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("could not convert to  a number")


