age = 12

if age < 4:
    price = 0
elif age < 18:  # 前面不通过，则会判断这个，这个通过后，跳过后面的
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
# 结尾的else也可换成elif

print("Your admission cost is $" + str(price) + ".")
