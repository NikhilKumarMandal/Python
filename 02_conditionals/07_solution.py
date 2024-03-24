order_size = "Medium"
extra_sort = True

if extra_sort:
    coffee = order_size + " coffee with extra short"
else:
    coffee = order_size + "coffee"

print("Order",coffee)