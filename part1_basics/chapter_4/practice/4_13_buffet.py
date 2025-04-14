buffet_foods = ('salmon', 'roast beef', 'salad', 'spaghetti', 'fruit')
for food in buffet_foods:
    print(food)

print('-'*50)
buffet_list = list(buffet_foods)  # 转换成列表
buffet_list[1] = "sushi"
buffet_list[3] = "fried rice"  # 赋值
buffet_foods = tuple(buffet_list)  # 转换回元组
# 或者直接对整个元组重新赋值
for food in buffet_foods:
    print(food)
