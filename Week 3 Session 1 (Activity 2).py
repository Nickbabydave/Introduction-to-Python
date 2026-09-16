# Exercise (Byte Cafe)
orders = []
while True:
    item = input("Enter item name of ordered: ")
    orders.append(item)
    choice = input("Would you like to enter another order? (y/n): ")
    if choice.lower() == "n":
        break
    print("\norders entered: ", orders)
    print(item)



