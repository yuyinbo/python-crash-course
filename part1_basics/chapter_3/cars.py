cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # 修改原列表
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)  # 添加参数reverse，倒序
print(cars)

# 使用sorted进行临时排序，返回的是新列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original lst:")
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nReverse')
print(sorted(cars, reverse=True))

print('\nHere s the original list again:')
print(cars)

print('-'*50)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()  # 并非排序，只是反转
print(cars)
print('len='+str(len(cars)))
