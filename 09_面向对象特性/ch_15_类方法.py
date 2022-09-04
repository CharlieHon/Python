class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    @classmethod
    def show_tool_count(cls):

        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name) -> None:
        self.name = name

        # 每次创建对象都会调用初始化方法
        Tool.count += 1


# 创建工具对象
tool1 = Tool("锤子")
tool2 = Tool("榔头")

# 调用类方法
Tool.show_tool_count()