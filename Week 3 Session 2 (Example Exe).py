# Example
# (Creating Function)

# def greeting():
#   print("Hello World")
# greeting()

# Example 1
# (input from the user and prints their sum using a function name “total”)

# x = int(input("Enter a number: "))
# y = int(input("Enter another number: "))
# def sum():
#     z = x + y
#     print(z)
# sum()

# Example 2

# PI = 3.142
# radius = float(input("Enter the radius: "))

# def area_of_circle():
#     area = PI *(radius**2)
#     print(f"The area of the circle is {area}")
# area_of_circle()

# Example 3
# (function with single parameter)

# def check_number(number):
#     if number % 2 == 0:
#         print(number, "is even.")
#     else:
#         print(number, "is odd.")
# number = int(input("Enter a number: "))
# check_number(number)

# Example 4
#(function with multiple parameters)

# def calculate_area(length, width):
#     area = length * width
#     print(area)
# length = int(input("Enter the length: "))
# width = int(input("Enter the width: "))
# calculate_area(length, width)

# Example 5
# (Return value)

# def divide(a,b):
#     if b == 0:
#         return "cannot divide by zero"
#     return a / b
# a = float(input("Enter the value of a: "))
# b = float(input("Enter the value of b: "))
# price = (divide(a,b))
# print(price)

# Example 6
# (takes a number as input and prints its multiplication table)

# def multipply():
#     i =1
#     number = int(input("Enter a number: "))
#     while i <= 10:
#       table = number * i
#       print(number, "x" ,i, "=",table)
#       i += 1
# multipply()

# Example 7
# (Write two Python functions in your program)
# (one to get the maximum number from the list below )
# (and the other to get minimum number from the list)

# score = [68, 74, 55, 30, 78, 90, 60]
# def maximum():
#     print("maximum score:", max(score))
# maximum()
#
# def minimum():
#     print("minimum score:", min (score))
# minimum()

# Example 8
# (create a Python function to
# find the sum of all positive numbers)

numbers = [6, 4, 5, 3, -4, -2, 5, 2, -6, 4]
def total():
    sum = 0
    for i in numbers:
        if i > 0:
            sum = sum + i
        print(sum)
total()













# Ex 6
# def multyply():
#   i = 1
#   number = int(input("Enter a number: "))
#   while i <= 10:
#       table = number * i
#       print(number, "x", i, "=", table)
#       i += 1
# multyply()



