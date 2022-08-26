name_list = ["张三", "李四", "王五", "张三"]

# len(length 长度) 函数可以统计列表中元素的总数
list_len = len(name_list)
print("列表中包含 %d 个元素" % list_len)

# count 方法可以统计列表中某一个数据出现的次数
count = name_list.count("张三")
print("张三出现了 %d 次" % count)

# 从列表中删除数据，如果值不存在则报错
name_list.remove("张三")
print(name_list)