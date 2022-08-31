def demo1():

    # 定义一个局部变量
    # 1> 出生：执行了下方代码之后，，才会被创建
    # 2> 死亡：函数执行完成之后
    num = 10
    print("在demo1函数内部的变量是 %d" % num)


def demo2():

    # 不能在其他函数内使用
    # print("%d" % num)
    pass

# 在函数内部定义的变量，不能再其他位置使用
# print("%d" % num)

demo1()
demo2()