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
print(x)
x1 = [i + 1 for i in range(10)]
print(x1)

# 用循环语句实现上面的代码
x2 = []
for i in range(10):
    x2.append(i + 1)
print(x2)
