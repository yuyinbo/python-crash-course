prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""  # 设置为空字符串，以使首次运行while时有可供检查的东西
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
