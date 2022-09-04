class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    def __init__(self, name) -> None:
        self.name = name

        # 每次创建对象都会调用初始化方法
        Tool.count += 1


# 1.创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("锤子")
tool3 = Tool("水桶")

# 2.输出工具对象的数量
# print(Tool.count)
print("工具对象总数：%d" % tool1.count)