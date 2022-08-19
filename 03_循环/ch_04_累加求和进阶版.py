# 计算 0~100 之间 所有 偶数 的累计求和结果
i, sum = 0, 0
while i <= 100:
    # 判断变量 i 中的数值，是否是一个偶数
    # 偶数 i % 2 == 0
    # 奇数 i % 2 != 0
    if i % 2 == 0:
        print(i)
        sum += i
    i += 1
print("sum = %d" % sum)