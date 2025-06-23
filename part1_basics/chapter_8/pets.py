def describe_pet(animal_type, pet_name):
    """宠物信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")


describe_pet('hamster', 'harry')
print()
# 关键字实参，顺序可以不同
describe_pet(pet_name='willie', animal_type='dog')


def describe_pet_2(pet_name, animal_type='dog'):
    """使用默认值"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")


print()
describe_pet_2('greg')
describe_pet_2('frank', 'cat')





















