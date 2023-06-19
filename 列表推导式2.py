# 复习创建二维列表
A = [0] * 3
for i in range(3):
    A[i] = [0] * 3
print(A)
A[1][1] = 5
print(A)

# 利用列表推导式创建二维列表
A = [[0] * 3 for i in range(3)]
print(A)
A[0][0] = 10
print(A)