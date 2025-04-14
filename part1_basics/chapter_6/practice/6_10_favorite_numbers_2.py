favorite_numbers = {
    "Shuen": [120, 150, 148],
    "Qingyi": [25, 26, 27],
    "Evelyn": [42, 61, 65],
    "Astra": [62, 63, 64],
}

for name, numbers in favorite_numbers.items():
    print(name+"'s favorite numbers are: ")
    for number in numbers:
        print("\t"+str(number))
