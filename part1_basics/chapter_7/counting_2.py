current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  # 如果是偶数，则跳到下一轮（的开头）

    print(current_number)
