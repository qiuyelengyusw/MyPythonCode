#打印输出字符串中的每一个字符
for each in "Qiuyelengyu":
    print(each)
print()
#用while循环语句实现同样的功能
str = "Qiuyelengyu"
length = len(str)
index = 0
while index < length:
    print(str[index])
    index += 1
#for循环和while循环的区别

#用for循环打印输出1到100之间的奇数
for i in range(1,101):
    if i % 2 == 1:
        print(i)
#用for循环实现1到1000之间所有数的和
sum = 0
for i in range(1,1001):
    sum += i # sum = sum + i
print(sum)
#for循环求1到10之间所有奇数的和
sum = 0
for i in range(1,11):
    if i % 2 == 1:
        sum += i
print(sum) # 输出结果为25
# for循环求1到10之间所有偶数的和
sum = 0
for i in range(1,11):
     if i % 2 == 0:
         sum += i
print(sum)  # 输出结果为30

# for循环实现1到10之间所有偶数的乘积
sum = 1
for i in range(1,11):
    if i % 2 == 0:
        sum *= i
print(sum) # 输出结果为480

#for循环实现1到10之间所有奇数的乘积
sum = 1 #乘积的初始值为1
for i in range(1,11):  #range(1,11)表示1到10之间的所有数
    if i % 2 == 1:     #判断i是否为奇数
        sum *= i       #如果i为奇数，则将i乘以sum的值，然后将结果赋值给sum
print(sum)            # 输出sum的值
