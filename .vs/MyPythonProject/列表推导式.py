# 将一个列表中的所有元素的值都乘以2
# 下面的代码是用自己的方法实现此功能，用循环语句
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(lista)):
    print(i)
    lista[i] = lista[i] * 2
print(lista)
print('*********************************************')
# 下面的代码用列表推导式来实现将列表中的元素值都乘以2
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = [i * 2 for i in lista]
print(lista)
lista = [i * 5 for i in lista]
print(lista)
x = [i for i in range(10)]
print("*************************")
print(x)
print('*************************')
x1 = [i + 1 for i in range(10)]
print(x1)
print('**************************')
# 用循环语句实现上面的代码
x2 = []
for i in range(10):
    x2.append(i + 1)
print(x2)

y = [a * 2 for a in "Fuck"]
print(y)
for each in y:
    print(each, end='')
print()
print('**************************')
code = [ord(c) for c in 'fuck']  # ord函数的作用是将单个字符串转换成对应的编码
print(code)
print('**************************')
print('使用列表推导式将下面的二位列表中的某列中的元素元素提取出来')
# 使用列表推导式将下面的二位列表中的某列中的元素元素提取出来
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col1 = [row[0] for row in matrix]
print(col1)
for each in col1:
    print(each, end=' ')
print()
print('**************************')
print('**************************')

# 输出二维列表中的元素
print('输出二维列表中的元素')
flatten = [col1 for row in matrix for col1 in row]
print(flatten)
for each in flatten:
    print(each, end=' ')
print()
print('**************************')
print('**************************')
print('推导式if语句：查找并输出列表中包含某个字符的元素')
# 推导式if语句：查找并输出列表中包含某个字符的元素
words = ['Fuck', 'Fire', 'Chinese', 'Brother', 'Find', 'Good']
fwords = [w for w in words if w[0] == 'F']
print(fwords)  # 输出新列表
# 输出列表中的元素
for each in fwords:
    print(each, end=' ')
print()
print('**************************')
print('**************************')
# 取出对角的元素，1，5，9
col3 = [matrix[i][i] for i in range(len(matrix))]
print(len(matrix))
print(col3)
print('**************************')
# 思考练习
# 输出 3，5，7
print('输出3, 5, 7')
col4 = [matrix[i][len(matrix) - i - 1] for i in range(len(matrix))]
print(col4)
print('**************************')

# 列表推导式嵌套的循环顺序举例：
print('# 列表推导式嵌套的循环顺序举例：')
flatten = [x + y for x in 'fuck' for y in 'Fire']
print(flatten)
print('**************************')
# 使用循环实现上面的代码：

# 定义一个空的列表
flattena = []
# 循环嵌套
for x in 'fuck':
    # 第一次循环，外层先取'f'，分别与内层的F ,i, r e 相组合
    for y in 'Fire':
        # 将组合后的元素，用append（）方法依次追加到新列表中
        flattena.append(x + y)
print(flattena)

print('**************************')
print('**************************')
print('列表推导式的终极语法')
# 列表推导式的终极语法
flattens = [[x, y] for x in range(10) if x % 2 == 0 for y in range(10) if y % 3 == 0]
print(flattens)
for each1 in flattens:
    for each2 in each1:
        print(each2, end=' ')

print()
print('**************************')
print('**************************')
print('将上面的推导式转换为循环的模式')
# 将上面的推导式转换为循环的模式
flattens = []
for x in range(10):
    if x % 2 == 0:
        for y in range(10):
            if y % 3 == 0:
                flattens.append([x, y])
print(flattens)
