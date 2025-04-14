pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:  # 字典名[键名]，访问值，这里是一个列表
    print("\t" + topping)

