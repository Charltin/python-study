# 列表推导式 嵌套for
# 外层循环在前 内层循环在后
# [expression for target1 in iterable1 if condition1
#             for target2 in iterable2 if condition2
#             for target3 in iterable3 if condition3
#                               ...
#             for targetN in iterableN if conditionN]

# 1. 列表的拍平
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 1.1 列表推导式
flatten = [col for row in matrix for col in row]
print('列表推导式-嵌套 flatten: ', flatten)

# 1.2 for循环
flatten = []
for row in matrix:
    for col in row:
        flatten.append(col)
print('for循环实现 flatten: ', flatten)

# 2. 栅栏密码
# TEOGSDYUTAENN HLNETAMSHVAED
couples = [x + y for x in 'TEOGSDYUTAENN' for y in 'HLNETAMSHVAED']
plain_text = couples[::len('HLNETAMSHVAED') + 1]
print('列表推导式-嵌套 栅栏密码: ', ''.join(plain_text))

# 3. 