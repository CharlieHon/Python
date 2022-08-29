for num in [1,2,3,4]:
    print(num)
    if num == 2:
        break
else:
    # 如果循环体内部使用break
    # else 下方的代码不会执行
    print("遍历")
print("循环结束")