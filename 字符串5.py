# 格式化字符串
# format()方法
year = 2023
x = '今年是 {} 年'.format(year)
print(x)
print()
x = '1+2 = {}, 2的平方等于{}, 3的立方等于{}'.format(1 + 2, 2 * 2, 3 * 3 * 3)
print(x)
x = '{}看到{}就很激动！'.format('mike', 'shit')
print(x)
print()
x = '{1}看到{0}就很激动！'.format('mike', 'shit')
print(x)
# {}是可以重复使用的
x = '{1}{0}{0}{1}'.format(1, 2)
print()
print(x)
print()
# format()的关键字
x = 'my name is {name}, i love {fav}'.format(name='john', fav= 'rose')
print(x)