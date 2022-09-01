def demo(num_list: list):
    print("函数内部的代码")

    # 使用方法修改列表的内容
    num_list.append(9)

    print(num_list)

    print("函数执行完成")

gl_list = [1, 2, 3]
demo(gl_list)
print(gl_list)