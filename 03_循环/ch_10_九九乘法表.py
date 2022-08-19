# 打印九九乘法表
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d" % (col, row, row * col), end="\t") # 使用横向制表位对齐文本
        col += 1
    print()
    row += 1
