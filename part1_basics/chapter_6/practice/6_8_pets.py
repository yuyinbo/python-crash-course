bella = {'name': 'bella', 'type': 'dog', 'owner': 'emily'}
whiskers = {'name': 'whiskers', 'type': 'cat', 'owner': 'jack'}
coco = {'name': 'coco', 'type': 'parrot', 'owner': 'sarah'}

pets = [bella, whiskers, coco]
for pet in pets:
    print(pet['owner'].title() + " has a " + pet['type'] + " called " + pet[
        'name'] + ".")
