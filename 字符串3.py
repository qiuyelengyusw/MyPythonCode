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