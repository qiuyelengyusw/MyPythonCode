# print("What's your name?")
# name = input()
# print("Your name is %s"%name)
# print("How old are you?")
# age = int(input())
# print("your age is"+ str(age))
# print("your age is %s"%age)
# print("your age is {}".format(age))
# print("you name is {0},you age is {1}".format(name,age))
# list = [1,2,3,4,"a","b","c",'a','b','c']
# print(list)
# # 一个字符串
# print("dahai"+"dsd")
# # 两个字符串
# print("dahai","dad")
# stra = "The real brave man"
# strb = "dare to face the wretched"
# strc = "and hopeless society and life."
# list1 = [stra,strb,strc]
# print(list1)
# print(stra+strb+strc)
# print(stra,strb,strc)
# print("".join(list1)) #一个字符串
# print(",".join(list1)) #用逗号分隔，
# print("**********".join(list1)) #用*分隔


#字符串的“改”
msg1 = "abc"
print(id(msg1))
print(msg1.lower())
print(id(msg1.lower()))
print(msg1.upper())
print(msg1.islower()) #判断字符串中的值是否全是小写
print(msg1.upper().isupper())  #判断字符串中的值是否全部为大写