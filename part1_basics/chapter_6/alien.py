alien_0 = {'color': 'green', 'points': 5}  # 值可以是任何类型的对象

print(alien_0['color'])
print(alien_0['points'])  # 字典名[键名]，用以访问值

new_points = alien_0['points']
print("You just earn " + str(new_points) + ' points!')

print(alien_0)

alien_0['x_pos'] = 0
alien_0['y_pos'] = 25
print(alien_0)

alien_1 = {}  # 定义空字典以存储用户数据或自动生成大量键值对

alien_1['color'] = 'red'
alien_1['points'] = 10
print(alien_1)
# 改变键值对的值
alien_2 = {'color': 'green'}
print("The alien is " + alien_2['color'] + '.')

alien_2['color'] = 'yellow'
print("The alien is now " + alien_2['color'] + '.')
# 根据值来判断
alien_3 = {'x_pos': 0, 'y_pos': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_pos']))

if alien_3['speed'] == 'slow':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_3['x_pos'] = alien_3['x_pos'] + x_increment
print("New x-position: " + str(alien_3['x_pos']))
# 删除键值对
alien_4 = {'color': 'green', 'points': 5}
print(alien_4)

del alien_4['points']
print(alien_4)
