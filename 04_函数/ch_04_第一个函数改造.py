name = "小明"

# Python 解释器知道下方定义了一个函数
def say_hello():
    """打招呼"""
    print("hello 1")
    print("hello 2")
    print("hello 3")

print(name)

# 只有在程序中，主动调用函数，才会让函数执行
say_hello()

print(name)