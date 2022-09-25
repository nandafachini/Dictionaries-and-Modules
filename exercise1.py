# Fill in a dictionary with the information of 5 products.
# Use the product name as the key and the price as the value.
# Request the data from the user.
# Scroll through the dictionary and display the name of products priced over $50.00

products = {}

for x in range(5):
    name = input('Name of the product: ')
    price = float(input("Price of the product: $ "))
    products[name] = price

for x in products:
    if products.get(x) > 50:
        print(x)
