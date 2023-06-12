love = "yes"
while love == "yes":
    print("Do you love me today?")
    love = str(input())
i = 1
sumi = 0
while i <= 100:
    i += 1
    sumi += i
    print(i)
print(sumi)

while True:
    print('Can I exit?')
    answer1 = str(input())
    if answer1 == "yes":
        print('you can exit this')
        # 跳出循环体
        break
    else:
        print('shit!')

# 使用while 循环以及 continue 语句实现输出奇数
c = 0
while c < 100:
    c += 1
    if c % 2 == 0:
        continue  # 当 C 可以被2 整除的时候，跳过下面的print(c),重新回到条件判断语句，如果满足条件，继续执行循环体的语句
    print(c)
# 总结，break 语句作用是跳出整个循环体，而continue语句的作用是跳出本次循环，回到循环开始的判断条件语句，如果满足循环条件，则再次运行循环体内的代码


# else 语句在循环中的应用
d = 5
while d < 10:
    print('循环内，d 的值是：', d)
    d += 1
else:
    print('循环外，d 的值是：', d)

day = 1
while day <= 7:
    answer2 = input('今天你有好好学习了吗？')
    if answer2 != "yes":
        break
    day += 1
else:
    print('very good !')

# 循环结构的嵌套 nested loop
# 九九乘法表
e = 1
while e <= 9:
    f = 1
    while f <= e:
        print(f, '*', e, '=', e * f, end=" ")
        f += 1
    print()
    e += 1


