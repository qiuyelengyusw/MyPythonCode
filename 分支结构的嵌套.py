print('请输入你的年龄：')
aged = int(input())
print('请输入你的性别：（1-男，2-女）')
isMale = int(input())
if aged <= 18:
    print('抱歉，由于您未满18岁，禁止访问！')
else:
    if isMale == 1:
        print('可以随便观赏！')
    else:
        print('抱歉，这里应该不适合你！')
