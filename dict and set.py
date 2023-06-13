g = {'mike': 95, 'john': 85, 'sw': 100}
print(g['mike'])
print(g['sw'])

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
g['jike'] = 99
print(g['jike'])
print(g)

# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
g['jike'] = 97
print(g['jike'])
print(g)