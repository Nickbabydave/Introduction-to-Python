# Use the break() to trace program
# execution step by step inside  loop
import numbers

#Solution
total =0

for number in range(1,6):
    breakpoint()
    total = total + number
print("Final Total =", total)


