try:
    # 1. 提示用户输入一个整数
    num = int(input("输入一个整数："))

    # 2. 使用 `8` 除以用户输入的整数并且输出
    res = 8 / num

    print(res)
except ValueError:
    print("请输入正确的整数")
except Exception as result:
    print("未知错误 %s" % result)