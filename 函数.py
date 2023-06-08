def greet(name):  # 声明函数
    print("Hello" + " " + name)  # 编写函数的功能
    return  # 编写函数结束语句


def age_1(age):
    if age < 15:
        return "You can still be silly as a child！" #返回字符串
    else:
        return "You are already an adult，Count a little bit in your heart!"


print("What's your name？")
strName = input() #将用户输入的内容赋值给strName.
print("How Old Are You？")
intAge = int(input()) #类型转换
greet(strName) #调用函数
print(age_1(intAge))
