hello_str = "hello hello"

# 1.统计字符串长度
print(len(hello_str))   # 11

# 2.统计某个小字符串出现的次数
print(hello_str.count("llo"))   # 2
print(hello_str.count("abc"))   # 0

# 3.某一个字符串出现的位置
print(hello_str.index("llo"))   # 2
# 注意：如果使用index方法传递的子字符串不存在，程序会报错！
# print(hello_str.index("abc"))