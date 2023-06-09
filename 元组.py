rhyme = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'home')
print(rhyme)
for each in rhyme:
    print(each, end=' ')
print()

# 可以通过元组的下表来输出元组中元素的值
print(rhyme[0])
print(rhyme[len(rhyme) - 1])

# 元组中元素不可以修改
# 使用切片的方法
print(rhyme[:3])
print(rhyme[3:])
print()
print(rhyme[3:-1])
print(rhyme[:])
print()
print(rhyme[::-1])
print()
print(rhyme[::2])
print()
nums = (3, 1, 2, 4, 3, 6, 3)
# 查询 元素 ‘3’在元组中的数量有几个
print(nums.count(3))
print()
# index（）输出指定的元素在元组中的位置
heros = ('蜘蛛侠', '绿巨人', '钢铁侠')
print(heros.index('蜘蛛侠'))
print()
# 元组的拼接
s = (1, 2, 3)
t = (4, 5, 6)
st = s + t
print(st)
print()
print(st * 3)
print()
# 元组的嵌套
w = s, t
print(w)
print()
for i in w:
    for each in i:
        print(each, end=' ')
print()
print('类似列表推导式的方法')
s = (1, 2, 3, 4, 5)
print([each * 20 for each in s])
print()
print('元组的打包')
# 元组的打包
t = (123, 'FishC', 3.14)
print(t)

# 元组的解包，同样适用于列表和字符串
x, y, z = t
print(x)
print()
print(y)
print()
print(z)

a, b, c, d = "Fuck"
print(a + b + c + d)
print()

# 元组中元素的值是不可变的，但是如果元组中的元素指向可变的列表，那么列表中的值是可以改变的
s = [1, 2, 3]
t = [4, 5, 6]
st = (s, t)
print(st)
st[0][0] = 100
print(st)