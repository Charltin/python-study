# 九九乘法表
i = 1
print('九九乘法表: ')
while i <= 9:
    j = 1
    sum = ''
    while j <= i:
        sum += str(j) + ' * ' + str(i) + ' = ' + str(i * j) + '\t'
        j += 1
    else:
        print(sum)
    i += 1
else:
    print()

# 计算 100w 以内所有数字的和
print('计算 100w 以内所有数字的和: ', end='')
sum = 0
for i in range(1000001):
    sum += i
print(sum)
print()

# 找出 n 以内的所有素数
print('找出 n 以内的所有素数: ')
n = input("Please enter the range of prime numbers (n): ")
prime_range = int(n)
prime_list = []

for num in range(2, prime_range):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        prime_list.append(num)

print(', '.join(str(prime) for prime in prime_list))
print()
