class Cat:
    """这是一个猫类"""

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom = Cat()
tom.eat()
tom.drink()
print(tom)

# 再创建一个猫对象
jerry = Cat()
jerry.eat()
jerry.drink()
print(jerry)

snow = jerry
print(snow) # 与 jerry 指向同一个地址