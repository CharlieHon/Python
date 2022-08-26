name = ["宋江", "卢俊义", "吴用", "公孙胜"]

# 使用 del 关键字(delete)删除列表元素
# 提示：在日常开发中，要从列表删除数据，建议使用列表提供的方法
del name[3]

# del 本质上是用来将一个变量从内存中删除

s = "小明"
del s
# 注意：如果使用 del 关键字将变量从内存中删除
# 后续的代码就不能再使用这个变量了
# print(s)  # s is not defined

print(name)