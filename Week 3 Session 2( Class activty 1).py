# solution 1
# name = input("Enter your name:")
#
# def greet_user():
#     print(f"Hello {name}, welcome to programming")
# greet_user()

# Solution 2
def check_age():
  age = int(input("Enter your age:"))
  if age < 13:
      print("You are a child.")
  elif age <= 19:
      print("You are a teenager.")
  else:
      print("You are an adult.")
check_age()

