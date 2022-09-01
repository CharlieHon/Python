def demo(*args, **kwargs):

    print(args)
    print(kwargs)


# 元组/字典变量
gl_num = (1, 2, 3)
gl_dict = {"name":"小明", "age":18}

# 会将两个参数都传递给 *args
demo(gl_num, gl_dict)   

# 拆包语法，简化元组/自带你变量的传递
demo(*gl_num, **gl_dict)

# 等价于
demo(1, 2, 3, name="小明", age=18)