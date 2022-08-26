name_list = ["zhangsan", "lisi", "wangwu"]

# 1. 取值和取索引
print(name_list[2]) # wangwu

# 知道数据的内容，想确定数据在列表中的位置
# 使用index方法需要注意，如果传递的数据不在列表中，程序会报错！
print(name_list.index("lisi"))  # 1

# 2. 修改
name_list[1] = "李四"

# 不能通过索引添加数据
# name_list[3] = "zhoubo"

# 3. 增加
# append 方法可以向列表的末尾追加数据
name_list.append("哈士奇")
# insert 可以在列表的指定索引位置插入数据
name_list.insert(1, "小李广")
# extend 将其他列表的所有内容追加到指定列表的末尾
temp_list = ["宋江", "卢俊义", "吴用", "公孙胜"]
name_list.extend(temp_list)

# 4. 删除
# remove 可以从列表中删除指定数据
name_list.remove("李四")
# pop 默认可以将列表最后一个元素删除
name_list.pop()
# pop 可以指定要删除元素的索引
name_list.pop(1)
# clear 清空整个列表
name_list.clear()

print(name_list)