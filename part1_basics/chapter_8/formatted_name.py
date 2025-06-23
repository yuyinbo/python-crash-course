def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


def get_formatted_name_2(first_name, middle_name, last_name):
    """可选实参"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name_2('john', 'lee',
                                'hooker')
print(musician)


def get_formatted_name_3(first_name, last_name, middle_name=''):
    """可选实参"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name_3('Ludwig', 'Beethoven'
                                , 'von')
print(musician)

musician = get_formatted_name_3('jimi', 'hendrix')
print(musician)
