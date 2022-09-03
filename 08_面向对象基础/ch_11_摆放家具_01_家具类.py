class HouseItem:

    def __init__(self, name, area) -> None:
        
        self.name = name
        self.area = area
    
    def __str__(self) -> str:
        
        return "[%s] 占地 %.2f" % (self.name, self.area)


# 1.创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)