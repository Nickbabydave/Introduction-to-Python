# Exercise 1
numbers = [5, 10, 15, 20, 25, 30]
total = sum(numbers)
print(total)

# Exercise 2
numbers = [5, 10, 15, 20, 25, 30]
largest = max(numbers)
smallest = min(numbers)
print(largest)
print(smallest)

# Exercise 4
numbers = [5, 10, 15, 20, 25, 30]
if numbers == sorted(numbers):
    print("ascending order")
else:
    print("descending order")

# Exercise 3
numbers = [5, 10, 15, 20, 25, 30]
for number in numbers:
    print(number, numbers.count(number))
