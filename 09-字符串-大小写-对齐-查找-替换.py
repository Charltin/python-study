# 字符串

# 判断一个数是否是回文数
# n = input('Please enter the number: ')
# print('Palindrome number!') if n == n[::-1] else print('Not palindrome number!')

# 1. 字符串-大小写字母换来换去
print('字符串-大小写字母换来换去'.center(20, '一'))

s = 'Me llamo Lyv Xinyi'
print('原字符串: ', s)

capitalize_s = s.capitalize()  # 首字母大写，其他小写
print('capitalize_s: ', capitalize_s)

casefold_s = s.casefold()  # 全部转换为小写，除英语外也适用于其他语言(比如德语)
print('casefold_s: ', casefold_s)

title_s = s.title()  # 每个单词的首字母大写
print('title_s: ', title_s)

swapcase_s = s.swapcase()  # 大小写翻转
print('swapcase_s: ', swapcase_s)

upper_s = s.upper()  # 所有字母大写
print('upper_s: ', upper_s)

lower_s = s.lower()  # 所有字母小写，仅限于英文
print('lower_s: ', lower_s)

# 2. 字符串-左中右对齐
print('字符串-左中右对齐'.center(20, '一'))

str = 'ventidos'
print('原字符串: ', str)

print('center-15-@: ') # 居中对齐
print(str.center(15, '@'))

print('ljust-15-@: ') # 左对齐
print(str.ljust(15, '@'))

print('rjust-15-@: ') # 右对齐
print(str.rjust(15, '@'))

print('zfill(10): ') # 填充0
print('-100'.zfill(10))

# 3. 字符串-查找
print('字符串-查找'.center(20, '一'))

addr = 'Calle santo justo pastor 155 piso 1 Puerta 3, 46022, Valencia'
print('原字符串: ', addr)

print('count: ', addr.count('a')) # 字符串中a出现的次数
print('count(3, 10): ', addr.count('a', 3, 10)) # 字符串3-10之间a出现的次数

print('find: ', addr.find('a')) # 从左往右a第一次出现的下标
print('rfind: ', addr.rfind('a')) # 从右往左a第一次出现的下标
print('rfind: ', addr.rfind('z'))
# find 和 rfind 找不到的话返回-1

print('index: ', addr.index('a')) # 从左往右a第一次出现的下标
print('rindex: ', addr.rindex('a')) # 从右往左a第一次出现的下标
# print('rindex: ', addr.rindex('z'))
# index 和 rindex 找不到的话报错

# 4. 字符串-替换

# 4.1 expandtabs 使用空格替换制表符，并返回一个新的字符串
code = '''
    print('烟火')
    print('彩色')'''
print('code: ', code)

new_code = code.expandtabs(4)
print('expandtabs: ', new_code) 

# 4.2 replace 替换指定的字符
# replace(old, new, count=-1) count是替换的次数，默认全部替换
msg = 'Nacido el 25 de julio de 2000, 22 años'
print('msg:', msg)

replaced_msg = msg.replace('25 de julio de 2000', '19 de Enero de 2001')
print('replaced_msg: ', replaced_msg)

# 4.3 translate(table)
# maketrans 制作转换规则
translate_s = 'Weekend Night'.translate(str.maketrans('AaBbCcDdEeFfGg', '1234567890qwer', 'e')) # 替换后去除 e
print('translate_s: ', translate_s)

