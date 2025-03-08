for each in "China":
    print(each)

# 用for语句实现1到100的和
suma = 0
for a1 in range(101):
    suma += a1
    print(suma)

# 输出100以内所有的素数
for n1 in range(2, 100): # 2到100的整数
    for n2 in range(2, n1): # 2到n1的整数
        if n1 % n2 == 0: #  n1除以n2的余数为0
            break
    else:
        print(n1, '是一个素数')

for i in range(1, 6):
    print(i)
print("----------------------------------------")
import math

# 输出100以内所有的素数
for n1 in range(2, 100):
    is_prime = True
    # 只需要检查到n1的平方根
    for n2 in range(2, int(math.sqrt(n1)) + 1):
        if n1 % n2 == 0:
            is_prime = False
            break
    if is_prime:
        print(n1, '是一个素数')
