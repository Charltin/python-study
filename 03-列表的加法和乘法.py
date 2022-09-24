# 列表的加法乘法等

s = [1, 2, 3]
t = [4, 5, 6]

# 1. 列表的加法
# add_res = s + t
# print(add_res) 
# [1, 2, 3, 4, 5, 6]

# 2. 列表的乘法
# multi_res = s * 3
# print(multi_res) 
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 3. 列表的嵌套
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in matrix:
    for each in i:
        print(each, end='  ')
    print()

# 4. 创建一个空矩阵 3 * 3
A = [0] * 3
for i in range(0, 3):
    A[i] = [0] * 3
for i in A:
    for each in i:
        print(each, end=' ')
    print()
print('-----------------')

# 易错点————用*创建矩阵
# 错误写法示范
B = [[0] * 3] * 3
B[1][1] = 1
for i in B:
    for each in i:
        print(each, end=' ')
    print()
# A 和 B 的区别
print('A 的第一行和第二行是否是同一个对象: ', A[0] is A[1]) # False
print('B 的第一行和第二行是否是同一个对象: ', B[1] is B[2]) # True
# 解析: *号是对原列表的重复引用, 并不是拷贝，所以B中的列表指向的是同一个对象, 修改其中的一个, 剩下的几个也会被修改


# 159 881 348 46
# ciento cincuenta y nueve
# ochocientos ochenta y uno
# trescientos cuatrenta y ocho
# cuatrenta y seis
