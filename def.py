# 函数的使用
def hello():
    print("hello world!")


hello()


# 比较两个整数，并返回较大的值
def max(inta, intb):
    if inta > intb:
        return inta
    else:
        return intb


a = 12
b = 20
print(max(a, b))


# 打印传入的字符串
def printme(str):
    print(str)
    return


printme("this is my input")
printme("this is my input again")


# 传可变对象实例
# 可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：
def changeme(mylist):
    mylist.append([1, 2, 3, 4, 5, 6])
    print(mylist)
    return


mylist = [10, 20, 30, 40, 50, 60]
changeme(mylist)
print(mylist)


# 以下实例中演示了函数参数的使用不需要使用指定顺序：
def printinfo(name, age):
    print("Name:", name)
    print("Age:", age)
    return


printinfo(age=50, name="mike")


# 调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值：
def printinfo1(name1, age1=35):
    print("Name:", name1)
    print("Age:", age1)
    return


printinfo1(age1=60, name1="john")
print("---------------------------")
printinfo1(name1="rose")


# eturn 语句
# return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的 return 语句返回 None。之前的例子都没有示范如何返回数值，以下实例演示了 return 语句的用法：
def sum(arg1, arg2):
    total = arg1 + arg2
    print("def in：", total)
    return total


totot = sum(10, 20)
print("def out：", totot)
