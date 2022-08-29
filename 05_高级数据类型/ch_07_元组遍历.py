from distutils.log import info


info_tuple = ("宋江", "及时雨", "天魁星")

# 使用迭代遍历元组
for my_info in info_tuple:
    # 使用格式化字符串拼接 my_info 这个变量不方便！
    # 因为元组中通常保存的数据类型是不同的！
    print(my_info)
