class Cat:
    """这是一个猫类"""

    def __init__(self, name):
        print("调用初始化方法")
        self.name = name

    def eat(self):
        print("%s 爱吃鱼" % self.name)

# 使用类名()创建对象时，会自动调用初始化方法 __init__
tom = Cat("Tom")
print(tom.name)
tom.eat()

snow = Cat("Snow")
snow.eat()