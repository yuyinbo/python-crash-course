even_numbers = list(range(2, 11, 2))
print(even_numbers)  # 从2到11（-1），2为步长

print("The first three items in the list are:")
for even_number in even_numbers[0:3]:
    print(even_number)

print("Three items from the middle of the list are:")
for even_number in even_numbers[1:4]:
    print(even_number)

print("The last three items in the list are:")
for even_number in even_numbers[-3:]:
    print(even_number)
