# 待打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 打印每个设计
while unprinted_designs:
    current_design = unprinted_designs.pop()

    print("Print model: " + current_design)
    completed_models.append(current_design)

# 显示打印好的模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    