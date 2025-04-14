players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # 切片[i:j]是从第i个到第j-1个
print(players[:4])  # 从第0个到4-1个
print(players[2:])  # 从第2个到最后一个
print(players[-3:])  # 从倒数第三个到最后一个

print('-'*50)
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())  # 打印第0个到第2个

