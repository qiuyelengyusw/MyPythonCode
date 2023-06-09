List1 = [1, 2, 3, 4, 5]
List2 = [1, 2, 3, 4, 5, 'list']
print(List1)
print(List2)
print(len(List2))
for stx in List2:
    print(stx)

# 用while语句实现上面的代码
print('下面的代码使用while语句来实现上面的for语句的功能')
k = 0
while k < len(List2):  # len函数用来获取列表或者字符串的长度
    print(List2[k])
    k += 1
print('下面语句实现打印列表中指定位置的值')
print(List2[5])
print(List2[len(List2) - 2])
# 下面的语句与上面的语句实现同样的功能
print(List2[-5])

# 列表切片
print(List2[3:6])  # 打印列表中从第三个到第六个元素的值

# 实现列表输出的几种方法
print(List2[3:])
print(List2[:3])
print(List2[:])
print(List2[0:6:2])  # 第三个冒号为步进的值
print(List2[::2])
print(List2[::-2])
print(List2[::-1])  # 将整个列表倒序输出
