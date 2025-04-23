prompt = "\nPlease enter your age:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    age = input(prompt)

    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age < 12:
            price = 10
        else:
            price = 15
        print("You need to pay $" + str(price) + " for the ticket.")
