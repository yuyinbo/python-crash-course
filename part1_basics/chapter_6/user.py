user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():  # .items()返回键值对列表, 是.items()而非.item()
    # 返回的每一个键值对是一个元组
    # 分别将键和值保存在两个变量中
    print("\nKey: "+key)
    print("Value: "+value)
