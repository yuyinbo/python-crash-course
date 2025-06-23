def build_person(first_name, last_name, age=''):
    """返回一个包含一个人信息的字典"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix')
print(musician)
musician = build_person('jimi', 'hendrix', str(27))
print(musician)
