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
print()
# 字符串的方法
x = 'I love You'
# capitalize(): 将字符串的首字母变成大写，其他字母变成小写
print(x.capitalize())
print()
# casefold():返回一个新的字符串其中每个单词都变成小写
print(x.casefold())
print()
# title() 返回一个每个单词的首字母大写的字符串
print(x.title())
print()
# swapcase() ：返回一个新的字符串，将字符串中所有单词的大小写进行翻转
print(x.swapcase())
print()
# upper(): 返回一个新的字符串，将原字符串中所有字母都变成大写
print(x.upper())