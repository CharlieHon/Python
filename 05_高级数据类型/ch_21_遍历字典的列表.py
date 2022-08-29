students = [
    {"name":"阿土"},
    {"name":"小李"}
]

# 在学员列表中搜索指定的姓名
find_name = "阿乐"

for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)
        # 如果已经找到，就直接退出循环
        break
else:
    # 如果希望在搜索列表时，所有的字典检查之后，都没有发现需要搜索的目标
    # 还希望得到统一的提示
    print("没有找到 %s" % find_name)
print("循环结束")