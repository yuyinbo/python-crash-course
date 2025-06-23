def make_pizza(size, *toppings):
    # 先匹配位置形参和关键字形参，再将剩余实参收集到最后一个里
    # 即*args
    print("\nMaking a " + str(size) + "-inch pizza with the following"
                                      "toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
