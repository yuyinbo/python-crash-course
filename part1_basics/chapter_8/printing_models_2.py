def print_models(unprinted_designs, completed_models):
    """
    打印每个设计，直到没有未打印的设计
    打印每个设计后，将其移动到另一个列表
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprint_designs1 = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models1 = []
print_models(unprint_designs1, completed_models1)
show_completed_models(completed_models1)
print('*'*50)
unprint_designs2 = ['Keqing', 'Ganyu', 'Hutao']
completed_models2 = []
print_models(unprint_designs2[:], completed_models2)  # 传递副本，不修改原列表
show_completed_models(completed_models2)
print(unprint_designs2)
