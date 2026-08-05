print("Welcome to shopping cart")
cart = []
while True:
    item = input("Enter a cart item: ")
    if item.lower() == "done":
        break
    cart.append(item)
print("Type:", type(cart))
print("Total Items:", len(cart))
print("Cart:", cart)
tuple = tuple(cart)
print("Type:", type(tuple))
print("Items:",tuple)
print("Checkout")