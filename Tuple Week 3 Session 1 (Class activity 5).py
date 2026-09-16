# Product name, price, stock
# Solution
product1 = ("Keyboard", 25.99, 12)
product2 = ("Mouse", 14.50, 30)
product3 = ("Monitor", 120.00, 5)

products = [product1, product2, product3]

print("PRODUCTS AND PRICE")
for product in products:
    print(product[0], "£", product[1])

print("Low stock products")
for product in products:
    if product[2] < 10:
        print(product[0], "Stock:", product[2])
total_stock = 0
for product in products:
    total_stock += product[2]
print("Total_stock:", total_stock)






