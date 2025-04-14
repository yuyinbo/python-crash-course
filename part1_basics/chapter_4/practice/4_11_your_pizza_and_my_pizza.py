my_pizzas=['Margherita', 'Pepperoni', 'Hawaiian', 'Meat Lovers']
friend_pizzas = my_pizzas[:]
my_pizzas.append("BBQ Chicken")
friend_pizzas.append("Supreme")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
