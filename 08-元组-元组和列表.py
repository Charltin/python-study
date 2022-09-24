# 元组和列表
# 列表：增删改查
# 元组：查

# 1. 元组外面是括号() ('元素0', '元素1', '元素2', '元素3', '元素4', ...)
# 赋值的时候可以加括号也可以不加
tuple1 = '元素0', '元素1', '元素2', '元素3', '元素4'
tuple2 = ('元素0', '元素1', '元素2', '元素3', '元素4')
print(tuple1, tuple2)

# 2. 内容不可变
memories = ('追光', '笑容', '航班', '日落')
print('memories[0]: ', memories[0])
# memories[0] = '傅宣' # 会报错

# 3. 切片操作
print('切片操作: ', memories[::-1])

# 4. count
nums = [1, 2, 4, 7, 2, 1, 2, 14, 5, 2, 57, 4, 7856]
print('count: ', nums.count(2))

# 5. index
print('index: ', memories.index('日落'))

# 6. 拼接 重复 嵌套
s = (1, 2, 3)
t = (4, 5, 6)
w = s, t
print('拼接: ', s + t)
print('重复: ', s * 3)
print('嵌套: ', w)

# 7. 可迭代
print('可迭代 循环: ', end='')
for view in memories:
    print(view, end=' ')
print(';  ', end='可迭代 嵌套循环: ')

for i in w:
    for j in i:
        print(j, end=' ')
print()

# 8. 列表推导式
print('nums: ', nums)
double_nums = [num * 2 for num in nums]
print('列表推导式 double_nums: ', double_nums)

# 9. 如何生成只有一个元素的元组
test_1 = (728)
test_2 = (728,)
print('test_1 = (728): ', test_1, ', type: ', type(test_1))
print('test_2 = (728): ', test_2, ', type: ', type(test_2))

# 10. 打包和解包
# 打包就是把几个元素赋值到一个元组里; 解包就是将元组中的元素赋值出来
# 打包和解包是适用于任何类型的，列表也可以这样
print('打包的元组: ', memories)
ele_1, ele2, ele_3, ele_4 = memories
print('解包的元组: ', ele_1, ele2, ele_3, ele_4)

# 关于python的多重赋值: x, y = 10, 20
# 实现原理:
# _ = (10, 20) # 通过元组进行打包
# x, y = _ # 通过元组进行解包

# 11. 改变元组内元素的方式
list1 = [1, 2, 3]
list2 = [4, 5, 6]

tuple_change = (list1, list2)
print('元组内的数组: ', tuple_change)

tuple_change[0][0] = 'look!'
print('改变元组内的数组: ', tuple_change)

# 其原理是元组内列表的引用并没有改变，元组是不可变的，但是列表是可变的，所以元组内的列表依旧是可变的