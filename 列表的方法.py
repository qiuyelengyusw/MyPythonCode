# 一、增加 append()
Heros = ['钢铁侠', '绿巨人']
print(Heros)
Heros.append('黑寡妇')
print(Heros)

# extend() 方法,其参数必须是一个可迭代的对象，新的内容是追加到原列表最后一个元素的后面
Heros.extend(['鹰眼', '灭霸', '雷神'])
print(Heros)
Heros[len(Heros):] = ['7']
print(Heros)

Heros[len(Heros):] = [8, 9, 10]
Heros.extend([11, 12, 13])
print(Heros)

# 在列表的任意位置添加数据 insert()

Heros.insert(1, '蜘蛛侠')
print(Heros)
Heros.insert(0, '银河护卫队')
print(Heros)
Heros.insert(len(Heros), 14)
print(Heros)
Heros.insert(len(Heros) - 1, '这个元素的倒序插入的')
print(Heros)

# 删除元素
# remove()方法
# 如果列表中存在多个匹配的元素，那么它只会删除第一个相匹配的元素
# 如果指定的元素不存在，程序就会报错
Heros.remove('灭霸')
print(Heros)

# 删除列表中某个位置的元素 pop() 方法
Heros.append('灭霸')
print(Heros)
Heros.pop(len(Heros) - 1)
print(Heros)

# clear()----清空整个列表
# Heroes.clear()
# print(Heroes)

# 改变列表中元素的方法
Heros[len(Heros) - 1] = '十六'
print(Heros)

# 将列表中的元素按照从小到大的顺序排列
nums = [1, 3, 6, 5, 10, 2, 15, 11, 30]
nums.sort()
print(nums)

# 将列表中的元素按照从大到小的顺序排列
nums.reverse()
print(nums)
Heros.reverse()
print(Heros)

# 查找列表中元素的个数的方法： count()
print(nums.count(11))
print(Heros.count('雷神'))

# index()方法查找列表中元素的索引值
print(Heros.index('银河护卫队'))
# 将列表中元素'7'，替换成'神奇女侠'
Heros[Heros.index('7')] = '神奇女侠'
print(Heros)

# copy()拷贝列表
HerosCopy1 = Heros.copy()
print(Heros)
print("***************************")
print(HerosCopy1)
# 使用切片的方法实现列表的拷贝
HerosCopy2 = Heros[:]
print(HerosCopy2)
HerosCopy3 = Heros[3:]
print(HerosCopy3)
HerosCopy4 = Heros[:10]
print(HerosCopy4)
