# 字符串

# startswith/endswit
# 是否以xxx开头/结尾 (prefix[, start[, end]])/(suffix[, start[, end]])
s = 'wonderland'
print('s: ', s)

startswith_w = s.startswith(('w', 'land'))
print('startswith_w: ', startswith_w) 

endswith_land = s.endswith(('land', 'exploring'))
print('endswith_land: ', endswith_land)
print()

# istitle 字符串是否是title格式的
s = 'welcome to wonderland'
print('s: ', s)

print('istitle_s: ', s.istitle())
print('istitle_s.title: ', s.title().istitle())
print()

# isupper 字符串是否全部是大写
print('isupper_s: ', s.isupper())
print('isupper_s.upper: ', s.upper().isupper())

# islower 字符串是否全部是小写
print('islower_s: ', s.islower())
print()

# isalpha 字符串中是否只有字母
print('isalpha_s: ', s.isalpha())

# isspace 是否是空白字符串(空字符串不是空白字符串)
print('isspace_s: ', s.isspace())
print('isspace_space: ', '  \n  '.isspace())

# isprintable 是否是可打印字符(转义字符不可打印)
print('isprintable_s: ', s.isprintable())
print('isprintable_n: ', '\n'.isprintable())
print()

# isdecimal isdigit isnumeric 是否是数字, 三个判断尺度各不相同
x = '123'
print('x: ', x)
print('decimal_x: ', x.isdecimal())
print('digit_x: ', x.isdigit())
print('numeric_x: ', x.isnumeric())
print()

x = '2²'
print('x: ', x)
print('decimal_x: ', x.isdecimal())
print('digit_x: ', x.isdigit())
print('numeric_x: ', x.isnumeric())
print()

x = 'ⅠⅣⅤⅥⅦⅧⅨ'
print('x: ', x)
print('decimal_x: ', x.isdecimal())
print('digit_x: ', x.isdigit())
print('numeric_x: ', x.isnumeric())
print()

x = '②③④'
print('x: ', x)
print('decimal_x: ', x.isdecimal())
print('digit_x: ', x.isdigit())
print('numeric_x: ', x.isnumeric())
print()

x = '一二三'
print('x: ', x)
print('decimal_x: ', x.isdecimal())
print('digit_x: ', x.isdigit())
print('numeric_x: ', x.isnumeric())
print()

x = '壹贰叁'
print('x: ', x)
print('decimal_x: ', x.isdecimal())
print('digit_x: ', x.isdigit())
print('numeric_x: ', x.isnumeric())
print()

# isalnum
# isalpha, isdecimal, isdigit, isnumeric 中任意一个返回为 true 返回结果就是 true
print('isalnum_x', 'abc1232²Ⅵ②二贰'.isalnum())

# isidentifier 是否是一个合法的标识符
x = 'long long ago'
print(x, 'isidentifier:', x.isidentifier())
x = '中文'
print(x, 'isidentifier:', x.isidentifier())
x = '2pm'
print(x, 'isidentifier:', x.isidentifier())
x = '-'
print(x, 'isidentifier:', x.isidentifier())
x = '_'
print(x, 'isidentifier:', x.isidentifier())
print()

# isascii
x = 'Q'
print(x, 'isascii:', x.isascii())
x = '好'
print(x, 'isascii:', x.isascii())


# iskeyword 是否为python的保留字
import keyword
x = 'if'
print(x, 'iskeyword:', keyword.iskeyword(x))
x = 'list'
print(x, 'iskeyword:', keyword.iskeyword(x))