def print_num(num):

    print(num)
    # 递归的出口，当参数满足某个条件时，不再执行函数
    if num == 1:
        return 
    
    # 自己调用自己
    print_num(num - 1)
    print("完成 %d" % num)


print_num(3)