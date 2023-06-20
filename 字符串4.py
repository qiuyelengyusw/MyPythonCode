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
print(x.lstrip('w'))
print(x.rstrip('cn'))
print(x.strip('wcn'))
