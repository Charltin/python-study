# 字符串

# 1. 截取
# 前后特定字符的处理
# lstrip 左侧不留白; rstrip 右侧不留白; strip 两侧都不要留白
# (chars=None) 默认去除空白
x = '    The Cheshire Cat     '
print(x, 'lstrip:', x.lstrip())
print(x, 'rstrip:', x.rstrip())
print(x, 'strip:', x.strip())
x = 'aaaaaThe Cheshire Cataa'
print(x, 'lstrip_a:', x.lstrip('aeTh'))
print()

# 前后特定字符串的处理
# removeprefix/removesuffix 在字符串前/后截取特定的字符串
x = 'Maddest of hatters'
print(x, 'removeprefix:', x.removeprefix('Maddest'))
print(x, 'removesuffix:', x.removesuffix('hatters'))
print()

# 2. 拆分
x = 'Maddest of hatters'

# 2.1 partition 根据分隔符拆分成三元组
# partition(sep) 从左到右; rpartition(sep ) 从右到左
# 返回的是一个三元组, (分隔符左侧的内容, 分隔符, 分隔符右侧的内容)
print(x, 'partition:', x.partition(' '))
# 返回的是一个三元组, (分隔符左侧的内容, 分隔符, 分隔符右侧的内容)
print(x, 'rpartition:', x.rpartition(' '))

# 2.2 split 根据分隔符拆分成一个个元素的数组
# split/rsplit(sep=None, maxsplit(-1)) 默认分隔符为空字符串, 匹配全部分隔符
print(x, 'split:', x.split())
print(x, 'rsplit:', x.rsplit())
print(x, 'rsplit:', x.rsplit(' ', 1))

# 2.3 splitlines(keepends=False) 根据行分割
x = 'Welcome\nto\r\nwonderland'
print(x)
print('splitlines:', x.splitlines())
print('splitlines:', x.splitlines(True))  # 包括换行符

# 3. 拼接
list_join = ['welcome', 'to', 'wonderland']
tuple_join = ('Forest', 'cottages', 'castles', 'cards that can talk')

# 3.1 join
print(' '.join(list_join))
print(' and '.join(tuple_join))

# 拼接两个字符串 'welcome' -> 'welcomewelcome' 用join拼接的效率比用加法拼接高
''.join(['welcome', 'welcome'])