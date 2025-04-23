# while处理列表
unconfirmed_users = ['raiden', 'yoimia', 'ayaka']
confirmed_users = []

while unconfirmed_users:  # 只要列表中有元素，则返回True
    current_user = unconfirmed_users.pop()  # 从表尾开始pop

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())