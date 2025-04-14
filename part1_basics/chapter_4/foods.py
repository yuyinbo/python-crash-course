my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # 不指定索引提取切片，即复制（创建一个新对象，而不是引用）
# friend_foods = my_foods  #是引用
my_foods.append('cannoli')
friend_foods.append('ice cream')  # 两个列表是不同的对象

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
