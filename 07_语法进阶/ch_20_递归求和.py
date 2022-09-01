# 1. 定义一个函数 `sum_numbers`
# 2. 能够接受一个 `num` 的整数参数
# 3. 计算 `1+2+……num` 的结果

def sum_numbers(num):

    # 1.出口
    if num == 1:
        return 1
    
    # 2.数字的累加 num + (1 2 3 ... num-1)
    # 假设 sum_numbers 能够正确处理 1 2 ... num-1
    return num + sum_numbers(num-1)


res = sum_numbers(5)
print(res)