# startswith() 判断字符串中的指定字符是否出现在字符串的起始位置，输出 True 或者 False
x = '我正在学习python'
print(x.startswith('我'))
print(x.startswith('正在'))

# endswith() 用法与startswith()相反，判断字符串中指定的字符是否出现在字符串的末尾
print(x.endswith('python'))
print(x.endswith('习'))
print()
if x.startswith(('你', '我', '他')):
    print('总有人会喜欢Python的')
print()

# istitle() 判断字符串是否每个单词都是以大写字母开头，其余字母都是小写
x = 'I love python'
print(x.istitle())
print('I Love Python'.istitle())
print()
# isupper() 判断字符串中所有字母都是大写
print('I love Python'.isupper())
# 同时调用两个方法
print('I love python'.upper().isupper())
print('i love you'.upper())
print('I LOVE PYTHON'.isupper())
print()
# isalpha() 检测判断字符串中是否都是有字母构成
# 注意：空格在python里被认为不是字母
print('i love you '.isalpha())
print('ILovePython'.isalpha())
print()
# isspace() 判断字符串是否为一个空白字符串
print('I Love You'.isspace())
print(' '.isspace())
print()
# isprintable() 判断一个字符串中是否所有字符都是可以打印的
print('i love you'.isprintable())
# 转义字符不可以被打印
print('i love you\n '.isprintable())
print()

x = '12345'
print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())
print()
x = '一二三四五'
print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())
print()
# isidentifier() 判断一个字符串是否是合法的python标识符
print('I am a good men'.isidentifier())
print('I_am_a_good_man'.isidentifier())
print()
print('使用keyword模块的iskeyword()判断一个字符串是不是python的保留标识符')
# 使用keyword模块的iskeyword()判断一个字符串是不是python的保留标识符
import keyword

print(keyword.iskeyword('if'))
print(keyword.iskeyword('fuck'))
