while True:
    try:
        x = int(input("please input a int:"))
        print("your input is :", x)
        break
    except ValueError:
        print("your input is err,please input again!")  # 出现异常时执行的代码
    else:
        print("your input is :", x)  # 没有异常时执行代码
    finally:
        input("please click any key to exit")  # 不管有没有错误，都会执行此代码
