dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)
print('-'*50)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)  # 要修改元组内容，只能全部重新赋值
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
