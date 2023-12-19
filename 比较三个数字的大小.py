print("请输入第一个数字：")
numberONe = int(input())  # 将用户输入的内容转换为int类型
print("请输入第二个数字：")
numberTwo = int(input())
print("请输入第三个数字：")
numberThree = int(input())
if numberONe > numberTwo and numberONe > numberThree:  # 当第一个数字大于第二个数字，并且第一个数字也大于第三个数字的时候，说明第一个数字是最大值
    print("三个数字中最大的数字是：", numberONe)
elif numberTwo > numberONe > numberThree:              # 当第二个数字大于第一个也同时大于第三个数字的时候，说明第二个数字是最大值
    print("三个数字中最大的数字是：", numberTwo)
else:
    print("三个数字中最大的数字是：", numberThree)
