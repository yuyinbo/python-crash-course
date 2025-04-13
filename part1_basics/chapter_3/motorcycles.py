motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)  # 添加到末尾

motorcycles.insert(1,'QJ')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
# pop和del的区别在于，pop返回被删除的值（栈弹出）
print(popped_motorcycle)
print(motorcycles)

first_owned_motorcycle = motorcycles.pop(2)
print('The first motorcycle I owned was a '+first_owned_motorcycle.title()+'.')

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.remove('suzuki')
print(motorcycles)
# del删除，pop(i)弹出i处的，remove根据值来删除
