while True:
    i = 0
    try:
        intNumber = int(input("请输入一个数字："))
    except ValueError:
        print('输入错误！')
    else:
        while i < intNumber:
            print(i, '+', intNumber - i, '=', intNumber)
            i += 1
    print('稍等，下面还有一波')  # break
    for k in range(intNumber):
        print(k, '+', intNumber - k, '=', intNumber)
    break
