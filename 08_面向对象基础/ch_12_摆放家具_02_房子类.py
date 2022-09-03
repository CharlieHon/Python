class HouseItem:

    def __init__(self, name, area) -> None:
        
        self.name = name
        self.area = area
    
    def __str__(self) -> str:
        
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:

    def __init__(self, house_type, area) -> None:
        
        # 只有需要外部自定义初始值的属性才需要设置成初始化函数的形参
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具名称列表
        self.item_list = []
    
    def __str__(self) -> str:
        
        # Python 能自动地将一对括号内部地代码连接在一起
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                 % (self.house_type, self.area, 
                 self.free_area, self.item_list))

    def add_item(self, item):

        print("要添加 %s" % item)



# 1.创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)

# 2.创建房子对象
my_home = House("两室一厅", 60)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)