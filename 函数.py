def greet(name):  # 声明函数
    print("你好" + " " + name)  # 编写函数的功能
    return  # 编写函数结束语句


def age_1(age):
    if age < 15:
        return "你还是儿童，还可以犯傻！"
    else:
        return "你已经是个成年人了，心里有点儿数吧！"


print("请问你的名字叫什么？")
strName = input()
print("请问你的年龄是多少？")
intAge = int(input())
greet(strName)
print(age_1(intAge))
