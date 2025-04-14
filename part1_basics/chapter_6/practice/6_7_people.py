person_0 = {'first_name': 'Evelyn', 'last_name': 'Chevalier',
            'age': 20, 'city': 'New Eridu'}
person_1 = {'first_name': 'Astra', 'last_name': 'Yao',
            'age': 18, 'city': 'New Eridu'}
person_2 = {'first_name': 'Ei', 'last_name': 'Raiden',
            'age': 5000, 'city': 'Inazuma'}

people = [person_0, person_1, person_2]
for person in people:
    print(person['first_name'] + " " + person['last_name'] + " is " +
          str(person['age']) + ", lives in " + person['city'] + ".")
# 一定记得int插入字符串要转换成str
