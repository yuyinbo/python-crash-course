sandwich_orders = ["BLT Sandwich",
                   "Club Sandwich",
                   "Grilled Cheese Sandwich",
                   "Tuna Salad Sandwich"]
finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print("I made your " + sandwich_order.lower() + ".")
    finished_sandwiches.append(sandwich_order)

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
