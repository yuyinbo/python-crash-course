favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

planned = ['steve', 'tom', 'phil', 'sarah']
for name in planned:
    if name in favorite_languages.keys():
        print("Thank you for taking the survey, " + name.title() + ".")
    else:
        print(name.title() + ", please take our poll!")
