# Create a Python function -
# to find the square of each number in the list below)
# Q1(Square numbers)

# List_1 = [4, 2, 8, 6]
# def square_numbers():
#      for number in List_1:
#       square = number * number
#       print(square)
# square_numbers()

# Q2 (Leap year or not)
# def check_leap_year(year):
#     if year % 4 == 0:
#         print("It is a leap year")
#     else:
#         print("Not a leap year")
# year = int(input("Enter a year: "))
# check_leap_year(year)

# Q3 (Prime number)
# def check_prime(number):
#     if number < 2:
#         print("Not a prime number")
#     for i in range(2, number):
#         if number % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")
# number = int(input("Enter a number: "))
#
# check_prime(number)

# Q4
# name = "hello"
# text = input("Enter a text: ")
# reversed_text = text[::-1]
# print(reversed_text)

# Q5 (Palindrome)
# (A palindrome is a word -
# that is the same forwards and backwards)

# text = input("Enter a word:")
# reversed_text = text[::-1]
# if text == reversed_text:
#  print("It is a Palindrome")
# else:
#     print("Not a Palindrome")

# Q6 (Shopping list)
shopping_list = []
while True:
    items = input("Enter an items: ")
    if items == "done":
        break
    shopping_list.append(items)

def show_total(shopping_list):
    total = len(shopping_list)
    print("Total items: ", total)

show_total(shopping_list)










