# 序列 - 能够作用于序列的运算符和函数

# 序列包含: 字符串、列表和元组
# 字符串和元组是不可变序列, 列表是可变序列

# 1. 运算符 + *
print('string +: ''abc' + 'def')
print('string *: ''abc' * 3)
print('list +:', [1, 2, 3] + [4, 5, 6])
print('list *:', [1, 2, 3] * 3)
print('tuple +:', (1, 2, 3) + (4, 5, 6))
print('tuple *:', (1, 2, 3) * 3)
print()

l_1 = [1, 2, 3]
print('l_1 - id:', id(l_1))  # 4448630720
l_1 *= 2
print('l_1 *= 2 - id:', id(l_1))  # 4448630720
l_2 = [4, 5, 6]
print('l_2 - id:', id(l_2))  # 4448886720
l_2 = l_2 * 2
print('l_2 = l_2 * 2 - id:', id(l_2))  # 4448629120
print()

t_1 = (1, 2, 3)
print('t_1 - id:', id(t_1))  # 4448630720
t_1 *= 2
print('t_1 *= 2 - id:', id(t_1))  # 4448630720
t_2 = (4, 5, 6)
print('t_2 - id:', id(t_2))  # 4448886720
t_2 = t_2 * 2
print('t_2 = t_2 * 2 - id:', id(t_2))  # 4448629120
print()
