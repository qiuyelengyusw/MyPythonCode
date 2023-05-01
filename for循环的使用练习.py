TheSum: int = 0
for i in range(2, 1001):
    TheTemp: int = 0
    for j in range(2, 1001):
        if (i % j == 0) and (j < i):
            TheTemp = 0
            break
        else:
            TheTemp = i
    TheSum = TheSum + TheTemp
print("1到1000之间所有质数和和为:" + str(TheSum))
print("1到1000之间所有质数的和为：{0}".format(TheSum))
print("1到1000之间所有质数的和为:", format(TheSum))
print(TheSum)
