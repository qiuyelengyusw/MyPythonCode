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
# 使用列表推导式将下面的二位列表中的某列中的元素元素提取出来
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col1 = [row[0] for row in matrix]
print(col1)

# 取出对角的元素，1，5，9
col3 = [matrix[i][i] for i in range(len(matrix))]
print(len(matrix))
print(col3)
print('**************************')
# 思考练习
# 输出 3，5，7
# 20230619
col4 = [matrix[len(matrix)-i-1][len(matrix)-i-1] for i in range(len(matrix))]
print(col4)
