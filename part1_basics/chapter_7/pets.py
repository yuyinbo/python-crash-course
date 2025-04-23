pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:  # 只要pets中还有cat就True
    pets.remove('cat')

print(pets)
