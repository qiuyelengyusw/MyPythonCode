# 判断一个字符串是否为回文数
print('请输入一个数字：')
x = input()
var = '是回文数' if x == x[::-1] else '不是回文数'
print(var)
print()
# 上面的代码等同于下面的if语句
if x == x[::-1]:
    print('是回文数')
else:
    print('不是回文数')

# 字符串的方法
x = 'I love You'
# capitalize(): 将字符串的首字母变成大写，其他字符变成小写
print(x.capitalize())