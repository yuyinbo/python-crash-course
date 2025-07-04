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
