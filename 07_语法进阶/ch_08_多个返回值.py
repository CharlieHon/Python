def measure():
    """测量温度"""

    temp = 39
    wetness = 50

    # 元组 - 可以包含多个数据，因此可以使用元组让函数一次返回多个值
    # 如果函数返回的类型是元组，小括号可以省略
    # return (temp, wetness)
    return temp, wetness

# 元组
res = measure()
print(res)

# 需要单独的处理温度或者湿度
print(res[0])
print(res[1])

# 如果函数返回的类型是元组，同时希望单独的处理元组中的元素
# 可以使用多个变量，一次接受函数的返回结果
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)