# 列表推导式
# [expression for target in iterable]

demo_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print('demo_list: ', demo_list)

# 0. demo: 将列表中的每一项乘以2
# 0.1 利用循环
for i in range(len(demo_list)):
    demo_list[i] = demo_list[i] * 2
print('demo_list的每一项乘以2: ', demo_list)

# 0.2 利用列表推导式(代码行数更少 效率更高)
demo_list = [i * 2 for i in demo_list]
print('demo_list的每一项再乘以2: ', demo_list)

# 1. 列表推导式的应用(一维数组)
list1 = [i ** 2 for i in range(10)]
print('列表推导式 i ** 2: ', list1)

list2 = [i * 2 for i in 'TBC']
print('列表推导式 字符串处理: ', list2)

list3 = [ord(i) for i in 'TBC']  # ord 是将字符转化为对应的编码
print('列表推导式 ord每个字符', list3)

# 2. 列表推导式的应用(二维数组)
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col2 = [row[1] for row in matrix1]
print('列表推导式 数组矩阵的第二列', col2)

diag1 = [matrix1[i][i] for i in range(len(matrix1))]
print('列表推导式 数组矩阵的对角线\\', diag1)
diag2 = [matrix1[i][- 1 - i] for i in range(len(matrix1))]
print('列表推导式 数组矩阵的对角线/', diag2)

# 3. 列表推导式的应用(创建矩阵)
S = [[0] * 3 for i in range(3)]
print('列表推导式 3 * 3矩阵', S)
S[1][1] = 1
print('S[1][1] = 1: ', S)
