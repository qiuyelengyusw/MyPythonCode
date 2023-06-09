#while 语句
a, b = 0, 1
while b < 10:    
    a, b = b, a + b
    print(b)


list = [1,2,3,4,5,6,7,8,9,10]
it = iter(list)
for x in it:
    print(x ,end=" ")



#使用netx()函数

import sys #引入sys模块
list1 = [1,2,3,4,5,6,7,8,9,10]
it1 = iter(list1)
while True:
    try:
        print(next(it1))
    except StopIteration:
        sys.exit()