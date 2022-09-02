class Cat:
    """这是一个猫类"""

    def eat(self):
        # 哪一个对象调用方法，self 就是哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)


# 创建猫对象
tom = Cat()

# 可以使用 .属性名，通过赋值语句就可以了
tom.name = "Tom"

tom.eat()
tom.drink()
print(tom)

# 再创建一个猫对象
jerry = Cat()

jerry.name = "大懒猫"

jerry.eat()
jerry.drink()
print(jerry)

snow = jerry
print(snow) # 与 jerry 指向同一个地址

