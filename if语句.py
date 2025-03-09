
print('请输入你的分数：')
# 获取用户输入的分数
score = input()
# 上面两行代码也可以写成：
# score = input('请输入你的分数：')
# 将输入的分数转换为整数类型
score = int(score)
# 判断分数是否在0到60之间（不包含60）
if 0 <= score < 60:
    # 如果是，输出等级为D
    print('D')
# 判断分数是否在60到80之间（不包含80）
elif 60 <= score < 80:
    # 如果是，输出等级为C
    print('C')
# 判断分数是否在80到90之间（不包含90）
elif 80 <= score < 90:
    # 如果是，输出等级为B
    print('B')
# 判断分数是否在90到100之间（包含100）
elif 90 <= score <= 100:
    # 如果是，输出等级为A
    print('A')
# 如果分数不在0到100之间
else:
    # 输出提示信息
    print('你真是个大聪明！')
# 下面是if else 语句的另一种用法 <执行语句> if <条件> else <执行语句>
# 提示用户输入年龄
print('请输入你的年龄:')
# 获取用户输入的年龄并转换为整数类型
age1 = int(input())
# 如果年龄小于等于12岁，输出'好好学习，天天向上'，否则输出'欢迎观看'
print('好好学习，天天向上') if age1 <= 12 else print('欢迎观看')

# 练习 # 判断两个数字的大小
# 获取用户输入的第一个数字并转换为整数类型
a = int(input("请输入一个数字："))
# 获取用户输入的第二个数字并转换为整数类型
b = int(input("请在输入一个数字："))
# 输出两个数字中的最大值
print("最大的数字是：", b if a < b else a ) #if else 语句的另一种用法

print("----------------------")
print("练习：判断一个数是奇数还是偶数")

sum  = int(input("请输入一个数字："))
if sum % 2 == 0 :
     print(sum , "是偶数")
else:
    print(sum, "是奇数")


print("----------------------")
temperature = int(input("今天的温度是多少度："))
if temperature > 30:
    print("天气很热")
elif temperature < 30:
    print("天气不热")