current_users = ['burnice', 'astra', 'evelyn', 'ceaser', 'qingyi']
new_users = ['Astra', 'Evelyn', 'Keqing', 'Ganyu', 'Hutao']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user+" is not available, please try another.")
    else:
        print(new_user+" is available")
