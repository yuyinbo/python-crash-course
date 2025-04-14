places = ['Norway', 'Italy', 'New Zealand', 'Hokkaido', 'Kyushu']

print("Origin list:")
print(places)

print("Sorted list:")
print(sorted(places))

print("Origin list again:")
print(places)

print("Reversely sorted list:")
print(sorted(places, reverse=True))

print("Origin list again:")
print(places)

places.reverse()
print("Reverse:")
print(places)

places.reverse()
print("Origin:")
print(places)

print('-'*50)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
