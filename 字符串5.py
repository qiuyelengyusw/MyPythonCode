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
x = 'my name is {name}, i love {fav}'.format(name='john', fav='rose')
print(x)
print()
print('my name is {name}, i love {0}, The pople love {0} ,good lake'.format('python', name='your father'))
print()
# 单纯的输出{}
print('{}, {}, {}'.format(1, '{}', 3))
print()
print('{}, {{}}, {}'.format(1, 3))

print()
# 【align】对其的方式
print('{:^20}'.format(250))
print()
print('{1:>20}{0:<20}'.format(520, 250))
print()
print('{left:>20}{right:<20}'.format(left='520', right='250'))
print()
print('{:010}'.format(520))  # 只对数字有效，如果将 520 改成字符串，将会报错
print()
print('{1:$>20}{0:#<20}'.format(520, 250))
print()
print('{:+} {:-}'.format(520, -250))
print()
print('{:,}'.format(12345678))
print('{:_}'.format(123456789))
print()
# 限定小数点后一共有多少位，小数点截取位置采用四舍五入的方式
print('{:.2f}'.format(3.1465926))
print()
# 限定小数点前后一共有多少位，小数点截取位置采用四舍五入的方式
print('{:.2g}'.format(3.16415926))


