def test1():

    print("*" * 50)
    print("test 1")
    print("*" * 50)

def test2():

    print("-" * 50)
    print("test 2")

    # 函数的嵌套调用
    test1()

    print("-" * 50)

test2()