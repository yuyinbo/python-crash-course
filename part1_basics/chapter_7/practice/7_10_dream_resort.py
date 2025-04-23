dream_resorts = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    resort = input("If you could visit one place in the world, where would"
                   " you go? ")
    dream_resorts[name] = resort

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Result ---")
for name, resort in dream_resorts.items():
    print(name.title() + " would like to visit " + resort + ".")
