for each in "China":
    print(each)

# 用for语句实现1到100的和
suma = 0
for a1 in range(101):
    suma += a1
    print(suma)

# 输出100以内所有的素数
for n1 in range(2, 100):
    for n2 in range(2, n1):
        if n1 % n2 == 0:
            break
    else:
        print(n1, '是一个素数')
