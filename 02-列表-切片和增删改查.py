# python 列表

# 1. 列表切片
from dis import findlabels


demo_list = ['uno', 'dos', 'tres', 'cuatro', 'cinco',
             'seis', 'siete', 'ocho', 'nueve', 'diez']

print('切片1: ', demo_list[3:5])
# ['cuatro', 'cinco']
print('切片2: ', demo_list[::-1])
# ['diez', 'nueve', 'ocho', 'siete', 'seis', 'cinco', 'cuatro', 'tres', 'dos', 'uno']

# 2. 列表排序
num_list = [5, 3, 1, 6, 8, 2, 3, 9]

# 2.1 sort 从小到大排序
num_list.sort()
print('sort: ', num_list)
# [1, 2, 3, 3, 5, 6, 8, 9]

# 2.2 reverse 翻转
num_list.reverse()
print('reverse: ', num_list)
# [9, 8, 6, 5, 3, 3, 2, 1]

bookshelf = ['光明共和国', '南方列车']

# 3. 增 append extend insert

# 3.1 c 添加一个元素
bookshelf.append('山音')
bookshelf[len(bookshelf):] = ['雪国']  # 等价于append
print('append: ', bookshelf)

# 3.2 extend 添加多个元素
bookshelf.extend(['JavaScript百炼成仙', 'C语言修仙', 'Git权威指南'])
bookshelf[len(bookshelf):] = ['深入了解ES6', 'JavaScript高级程序设计(第六版)']  # 等价于extend
print('extend: ', bookshelf)

# 3.3 insert 在任意位置添加元素，第一个参数：插入位置，第二个参数：插入元素
bookshelf.insert(4, '我是猫')
print('insert: ', bookshelf)

# 4. 删 remove pop

# 4.1 remove 删除指定元素
bookshelf.remove('C语言修仙')
print('remove: ', bookshelf)

# 4.2 pop 删除指定位置的元素
bookshelf.pop(4)
print('pop: ', bookshelf)

# 4.3 clear 清空列表
# bookshelf.clear()
# print('clear: ', bookshelf)

# 5. 改 下标 切片

# 5.1 直接根据下标修改
bookshelf[3] = '海边的卡夫卡'
print('直接根据下标修改: ', bookshelf)

# 5.2 切片修改
bookshelf[3:] = ['我是猫', '1Q84']
print('切片修改: ', bookshelf)

# 6. 查
find_list = [1, 4, 5, 2, 1, 5, 2, 1, 5, 2, 7, 3, 6]
find_list.sort(reverse=True)

# 6.1 count 查找某个元素出现的次数
print('count(1): ', find_list.count(1))

# 6.2 index(x, start, end) 查找某个元素第一次出现的索引值
print('index(5): ', find_list.index(5), find_list)
print('index(5, 3, 12): ', find_list.index(5, 3, 12), find_list)

bookshelf[bookshelf.index('我是猫')] = '雪国'
print('index的应用: ', bookshelf)

# 6.3 copy 浅拷贝
nums_copy1 = find_list.copy()
print('copy: ', nums_copy1)
nums_copy2 = find_list[:]
print('切片实现copy: ', nums_copy2)
