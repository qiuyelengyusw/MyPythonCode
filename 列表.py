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
while k < len(List2):   #len函数用来获取列表或者字符串的长度
    print(List2[k])
    k += 1
