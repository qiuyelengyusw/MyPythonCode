# conut() 查找子字符串在字符串中出现的次数
x = '上海自来水来自海上'
print(x.count('海'))
print(x.count('海', 2, len(x)))
print()
# find()：从左向右找 rfind()：从右向左找 用于定位sub参数指定的子字符串在字符串中的索引下标值
print(x.find('自'))
print(x.rfind('自'))
print()
print(x.find('海', 0, len(x)))
print(x.find('海', 5, len(x)))
print(x.rfind('海', 5, len(x)))
print()
print(x.index('上'))
print()
# 字符串的替换方法
# expandtabs() 用空格来替换制表符，返回一个新的字符串
code = """
        print('I love you')
   print('I love my wife')"""
new_code = code.expandtabs(4)
print(new_code)
print()
print('在吗？我在你家楼下，快点下来！'.replace('在吗？', '想你！'))
# 比较复杂的替换方法
print('I love FishC'.translate(str.maketrans('ABCDEFG', '1234567')))
print()
print('I love FishC'.translate(str.maketrans('ABCDEFG', '1234567', 'love')))
