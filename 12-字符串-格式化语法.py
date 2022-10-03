# 字符串 
# format 专场

print('{0} and {1}'.format('Magical cabins', 'lovely white rabbits with clocks'))

# 大括号后的索引后面还有很多可以设置的参数，索引和参数中间用 : 分割
# [[fill]algin][sign][#][0][width][grouping_option][.precision][type]
# [[填充的字符]位置对齐参数][符号选项][#][宽度][千分位的分隔符][精度][输出类型]

# 1. algin: 位置对齐参数 和 width: 宽度
# ^  居中对齐  
# >  右对齐  
# <  左对齐
print('居中对齐: ', '{:^10}'.format(250)) # width 10
print('右对齐和左对齐: ', '{1:>10}{1:<10}'.format(250, 520))
print()

# 2. 0: 感知正负号0填充
print('正数0填充: ', '{:010}'.format(123))
print('负数0填充: ', '{:^010}'.format(-123))
print()

# 3. fill: 指定填充的字符
print('指定填充字符-%: ', '{:%>10}{:%<10}'.format(123, 321))
print('字符串填充0: ', '{:010}'.format('123'))
print('数字填充0: ', '{:010}'.format(123))
print()

# 4. sign: 符号选项, 仅对数字类型有效
# + 在正数前添加+, 负数前增加-
# - 只在负数前增加-, 默认行为
# 空格 在正数前添加一个空格，负数前添加一个负号
print('+ & -: ', '{:+} {:-}'.format(123, 321))
print('space: ', '{: }'.format(123))

# 5. grouping_option 千分位的分隔符可选 , 和 _
print('千分位分隔符: ', '{:,} and {:_}'.format(1234567, 8765432))
print()

# 6. .precision 精度选项, 不允许用在整数上
# f 小数点后多少位, 四舍五入
# g 小数点前后一共多少位, 科学计数法, 四舍五入
# 直接数字 对于非数字是限定最大字段的大小
print('precision f: ', '{:.2f}'.format(3.14159265358979323846264338327950288))
print('precision g: ', '{:.2g}'.format(12745673.14159265358979323846264338327950288))
print('非数值类型: ', '{:.5}'.format('welcome'))
print()

# 7. type

# 7.1 适用于整数:
# 'b' 二进制形式输出
# 'c' Unicode字符形式输出
# 'd' 十进制形式输出
# 'o' 八进制形式输出
# 'x' 十六进制形式输出
# 'X' 十六进制形式输出
# 'n' 和'd'类似，不同在于它会使用当前语言环境设置的分隔符插入到恰当的位置
# None 和'd'一样
# #号 在数字以非十进制输出的时候会自动增加一个前缀
print('8 - b: ''{:#b}'.format(8))
print('80 - c: ''{:c}'.format(80))
print('18 - d: ''{:d}'.format(18))
print('18 - o: ''{:#o}'.format(18))
print('18 - x: ''{:#x}'.format(18))
print('18 - X: ''{:#X}'.format(18))
print('314159 - n: ''{:n}'.format(314159))
print()

# 7.2 适用于浮点数
# 'e' 'E' 科学计数法形式输出，默认精度为6
# 'f' 'F' 定点表示法的形式输出，默认精度为6
# 'g' 'G' 通用格式，小数以'f'形式输出，大数以'e'形式输出
# 'n' 和'g'类似，不同在于它会使用当前语言环境设置的分隔符插入到恰当的位置
# '%' 百分比形式输出, 默认精度为6
# None 类似于g，但小数点后至少显示一位
print('e & E: ''{:e} {:E}'.format(8, 8))
print('f & F: ''{:f} {:F}'.format(8.132432, 8.132432))
print('g & G: ''{:g} {:G}'.format(8324123414.14234, 8321341234214.14234))
print('%: ''{:.2%}'.format(12.432679))
print()

# 8. 关键字传入参数
print('prec: ''{:.{prec}f}'.format(3.1415926, prec=4))
print('{:{fill}{align}{width}{grouping_option}.{prec}{type}}'.format(64198323.141592, fill='+', align='^', width=20, grouping_option='_', prec=6, type='g'))

