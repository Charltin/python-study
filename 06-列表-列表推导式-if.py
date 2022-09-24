# 列表推导式 使用if筛选
# [expression for target in iterable if condition]
# <1> 执行 for 语句
# <2> 执行 if 语句
# <3> 执行 expression

# odd_list 0~9的所有单数
odd_list = [i for i in range(10) if i % 2]
print('列表推导式-if 0~9的所有单数: ', odd_list)

# start_with_F 以F开头的字符串
words = ['Great', 'Fantastic', 'Brilliant', 'Unbelievable', 'Foolish']
start_with_F = [w for w in words if w[0] == 'F']
print('列表推导式-if 以F开头的字符串', start_with_F)