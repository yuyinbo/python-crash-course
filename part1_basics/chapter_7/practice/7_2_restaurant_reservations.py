number = input("May I ask how many guests will be joining us for dinner? ")
number = int(number)
if number > 8:
    print("I'm very sorry, but we currently do not have "
          "enough available tables.")
else:
    print("Certainly, we have sufficient seating for your group.")
