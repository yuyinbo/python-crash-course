prompt = "\nPlease enter the toppings you would like to add: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    topping = input(prompt)  # 必须要添加变量保存输入，否则每次input都要获取一次输入

    if topping == 'quit':
        break
    else:
        print("We will add "+topping.lower()+" to the pizza!")
