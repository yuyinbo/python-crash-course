favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      '.')

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
# 遍历所有键, 注意是.keys(), 它返回一个包含所有键的列表
for name in favorite_languages.keys():
    print(name.title())
# 默认遍历的就是键, .keys()增强了可读性
for name in favorite_languages:
    print(name.title())

print('-' * 50)
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is" +
              favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():  # .keys()返回的是一个列表, 包含了所有键
    print("Erin, please take our poll!")

print('-' * 50)
for name in sorted(favorite_languages.keys()):  # 遍历排序后的键列表
    print(name.title() + ", thank you for taking the poll.")

print('-' * 50)
print("The following languages have been mentioned:")
for language in favorite_languages.values():  # .values()返回列表，它包含了所有值
    print(language.title())
# 为了去除重复项，使用集合set
# 集合虽然是无序的，但可以迭代（不能set[0])
print()
for language in set(favorite_languages.values()):
    print(language.title())
