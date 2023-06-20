# 截取字符串

# lstrip() 去掉字符串左侧的空白
x = '     左侧不要留空白'
print(x)
print(x.lstrip())
print()
# rstrip() 去掉字符串右侧的空白
x = '右侧不要留空白       '
print(x)
print(x.rstrip())
print()
# strip()去掉字符串左右两侧的空白
x = '   两端都不要留空白    '
print(x)
print(x.strip())
print()

# 这三个方法可以传入参数
x = 'www.fuck.com.cn'
# 去掉字符串左边的W
print(x.lstrip('wcn.'))
print(x.rstrip('.cn'))
print(x.strip('wcn.'))
print()
print()
print(x.removeprefix('www.'))
print(x.removesuffix('.com.cn'))
print()
print()
# 拆分&拼接
print(x.partition('.'))
print(x.rpartition('.'))
print()
print(x.split())
print(x.split('.'))
print(x.split('.', 1))
print(x.split('.', 2))
print(x.rsplit('.', 1))
print(x.rsplit('.', 2))
x = 'www\r\nfuck\ncom\ncn'
print(x)
print(x.split('\n'))
print(x.splitlines())
print()
# join()
# 用列表
x = '.'.join(['www', 'fuck', 'com', 'cn'])
print(x)
print()
# 用元组也可以
x = '.'.join(('www', 'fuck', 'com', 'cn'))
print(x)
print()
# 字符串拼接的两种方法
x = 'fuck'
x += x
print(x)
print()
# 使用join（）
x = ''.join(('fuck', 'fuck'))
print(x)