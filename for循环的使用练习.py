TheSum: int = 0  #定义一个参数用来存储和
for i in range(2, 1001):
    TheTemp: int = 0 #定义一个临时参数
    for j in range(2, 1001):
        if (i % j == 0) and (j < i):
            TheTemp = 0
            break   #跳出循环
        else:
            TheTemp = i
    TheSum = TheSum + TheTemp #计算和 这里需要注意缩进，如果缩进错误，则计算数值出错
#以下是print语句个各种用法
print("1到1000之间所有质数和和为:" + str(TheSum))
print("1到1000之间所有质数的和为：{0}".format(TheSum))
print("1到1000之间所有质数的和为:", format(TheSum))
print(TheSum)
