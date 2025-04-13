name = "evelyn chevalier"
print(name.title())
print(id(name))
print(id(name.title()))  # 返回的是一个新变量，原变量没有更改
print(name.upper())
print(name.lower())

name1 = "Astra Yao"
name2 = "astra yao"
print(name1.lower() == name2.lower())  # 可用这种方式来处理大小写

first_name = "evelyn"
last_name = "chevalier"
full_name = first_name + " " + last_name
print("I love you, "+full_name.title()+"!")

print("Languages:\n\tPython\n\tC\n\tJavaScript")  # 练习换行符和制表符

favorite_language = " Python "
print(favorite_language+"|")
print(favorite_language.rstrip()+"|")  # 删除右边空格
print(favorite_language.lstrip()+"|")  # 删除左边空格
print(favorite_language.strip()+"|")  # 删除左右空格
