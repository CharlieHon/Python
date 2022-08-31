# 全局变量
num = 10

def demo1():

    # 修改全局变量的值
    # 在 python 中，不允许直接修改全局变量的值
    # 如果使用赋值语句，会在函数内部，定义一个局部变量
    num = 99
    print("demo1() ==> %d" % num)


def demo2():

    print("demo2() ==> %d" % num)

demo1()
demo2()