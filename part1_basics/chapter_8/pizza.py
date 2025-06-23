def make_pizza(*toppings):  # 创建一个空元组，并将所有收到的值封装到这个元组中
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')
