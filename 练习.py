# print("What's your name?")
# name = input()
# print("Your name is %s"%name)
# print("How old are you?")
# age = int(input())
# print("your age is"+ str(age))
# print("your age is %s"%age)
# print("your age is {}".format(age))
# print("you name is {0},you age is {1}".format(name,age))
# list = [1,2,3,4,"a","b","c",'a','b','c']
# print(list)
# # 一个字符串
# print("dahai"+"dsd")
# # 两个字符串
# print("dahai","dad")
# stra = "The real brave man"
# strb = "dare to face the wretched"
# strc = "and hopeless society and life."
# list1 = [stra,strb,strc]
# print(list1)
# print(stra+strb+strc)
# print(stra,strb,strc)
# print("".join(list1)) #一个字符串
# print(",".join(list1)) #用逗号分隔字符
# print("**********".join(list1)) #用*分隔字符


# 字符串的“改”
msg1 = "abc"
print(id(msg1))
print(msg1.lower())
print(id(msg1.lower()))
print(msg1.upper())
print(msg1.islower())  # 判断字符串中的值是否全是小写
print(msg1.upper().isupper())  # 判断字符串中的值是否全部为大写
strd = "0123456789"
print(strd[0:-1])  # 输出第一个到倒数第二个的所有字符
print(strd[0])  # 输出字符串第一个字符
print(strd[2:5]) # 输出从第三个开始到第五个的字符
print(strd[1:8:2])  # 输出从第二个开始到第八个，每隔一个的字符（步长为2）
print("\n")
print(strd * 2)
a = 123
print(isinstance(a, int)) #判断a是否为int类型
IntA = 21
IntB = 10
IntC = 0
if (IntA == IntB):
    print("IntA = IntB")
else:
    print("IntA != IntB")
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
if (IntA in list2):
    print('IntA在列表list2中')
else:
    print('IntA不在列表list2中')
x = True
y = False
z = False
if x or y and z:  # 先计算 y and z 返回False ,然后 x or False ,返回True
    print("Yes")
else:
    print("No")

# 更新字符串
var1 = "Hello World!"
print(var1)
print("Hello\b World!")
print("已经将字符串更新为：", var1[:6] + "Runoob!")
list11 = ['Google', 'Runoob', 1997, 2000, 2023]
list12 = [1, 2, 3, 4, 5]
list13 = ["a", "b", "c", "d"]
list14 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(list11[0])
print(list11[1])
print(list11[2])
print(list11[3])
tup1 = (50)
print(type(tup1))
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
tup2 = (10, 11, 12, 20)
tup3 = ("a", "b", "c")
tup4 = tup2 + tup3
print(tup4)
print(min(tup2))
print(max(tup2))
print(len(tup2))  # 计算元组元素个数

# 字典，字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

# 两个重要的点需要记住：
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
tinydict1 = {"A": 123, 98.6: 37, "B": 456}
print(tinydict1)
print(len(tinydict1))
print(tinydict1["A"])  # 输出“A”的值
print(tinydict1["B"], tinydict1[98.6])
tinydict1["A"] = 123123  # 修改
tinydict1["C"] = 456456  # 添加信息
del tinydict1[98.6]  # 删除键
print(tinydict1)

# 集合：
# 将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
thisset = set(("Google", "Ruoob", "Taobao"))
thisset.add("Facebook")
print(thisset)

# 条件控制

# if
age1 = int(input("Your dog's age:"))
print("")
if age1 <= 0:
    print("Are you kidding me?")
elif age1 == 1:
    print("Equivalent to a 14-year-old man")
elif age1 == 2:
    print("Equivalent to a 22-year-old man")
elif age1 > 2:
    human = 22 + (age1 - 2) * 5
    print("Equivalent to a ", human, "-year-old man")
input("click enter exit")

# 循环语句
# while python中没有do while 循环语句
a = 1
while a < 10:
    print(a)
    a += 1

# 用while循环计算从1到100所有整数的和
n = 100
sum1 = 0
counter1 = 1
while counter1 <= n:
    sum1 = sum1 + counter1
    counter1 += 1
print("1 到 %d 之和为：%d" % (n, sum1))

# while 中使用break:
n1 = 5
while n1 > 0:
    n1 += 1
    if n1 >= 200:
        break
    print(n1)
print("While is over")

# 在while中使用continue:
n2 = 500
while n2 > 0:
    n2 -= 1
    if n2 <= 10:
        continue
    print(n2)
print("While is over")

# for 循环语句
sites11 = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites11:
    print(site)

world1 = "1234567890"
for letter in world1:
    print(letter)

for number in range(1, 11):
    print(number)

for x in range(101):
    print(x)
else:
    print("Finally finished!")
