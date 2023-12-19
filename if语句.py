print('请输入你的分数：')
score = input()
# 上面两行代码也可以写成：
# score = input('请输入你的分数：')
score = int(score)
if 0 <= score < 60:
    print('D')
elif 60 <= score < 80:
    print('C')
elif 80 <= score < 90:
    print('B')
elif 90 <= score <= 100:
    print('A')
else:
    print('你真是个大聪明！')
# 下面是if else 语句的另一种用法 <执行语句> if <条件> else <执行语句>
print('请输入你的年龄:')
age1 = int(input())
print('好好学习，天天向上') if age1 <= 12 else print('欢迎观看')

# 练习
a, b = 30, 5  # 判断两个数字的大小
print(a) if a < b else print(b)
