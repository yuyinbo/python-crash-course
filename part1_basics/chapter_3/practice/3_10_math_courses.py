math_courses = ['Calculus', 'Linear Algebra', 'Probability',
                'Numerical Analysis', 'Abstract Algebra']
print('First courses: ', math_courses[0])
print('Last courses: ', math_courses[-1])
# 更改最后一个
math_courses[-1] = 'Differential Equations'
print('After modification: ', math_courses)
# 添加
math_courses.append('Abstract Algebra')
print('After append: ', math_courses)
# 插入
math_courses.insert(0, 'Set Theory')
print('After insert: ', math_courses)
# 按值删除
math_courses.remove('Probability')
print('After remove: ', math_courses)
# 删除
del math_courses[0]
print('After del: ', math_courses)
# 弹出（特定位置）
popped_course = math_courses.pop(-2)
print('Popped: ', popped_course)
print('After pop: ', math_courses)
# 暂时排序
print('Temporarily sorted: ', sorted(math_courses))
# 永久排序
math_courses.sort()
print('After sort: ', math_courses)
# 反向排序
math_courses.sort(reverse=True)
print('Reverse sort: ', math_courses)

math_courses = ['Calculus', 'Linear Algebra', 'Probability',
                'Numerical Analysis', 'Abstract Algebra']
# 倒序
print("After reversed: ", math_courses.reverse())
# 长度
print("Total number: ", len(math_courses))
