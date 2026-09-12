x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
operator = input("choose operator(+,-,*,/):")

if operator == "+":
    print("Result:", x + y)
elif operator == "-":
    print("Result:", x - y)
elif operator == "*":
    print("Result:", x * y)
elif operator == "/":
    print("Result:", x / y)
else:
    print("Invalid operator")

