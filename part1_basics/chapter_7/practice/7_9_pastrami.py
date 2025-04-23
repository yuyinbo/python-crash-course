sandwich_orders = ["BLT Sandwich",
                   "Pastrami",
                   "Club Sandwich",
                   "Pastrami",
                   "Pastrami",
                   "Grilled Cheese Sandwich",
                   "Tuna Salad Sandwich"]
finished_sandwiches = []

print("The pastrami has sold out.")
orders = [sandwich_order.lower() for sandwich_order in sandwich_orders]

while "pastrami" in orders:
    orders.remove('pastrami')

while orders:
    order = orders.pop()
    if order == "blt sandwich":
        finished_sandwiches.append("BLT Sandwich")
    else:
        finished_sandwiches.append(order.title())

print(finished_sandwiches)
