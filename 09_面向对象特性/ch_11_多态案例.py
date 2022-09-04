class Dog(object):

    def __init__(self, name) -> None:
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳地玩耍..." % self.name)


class XiaoTianDog(Dog):

    def game(self):
        print("%s 飞到天上玩耍..." % self.name)


class Person(object):

    def __init__(self, name) -> None:
        self.name = name

    def game_with_dog(self, dog: Dog):
        print("%s 和 %s 快乐地玩耍..." % (self.name, dog.name))
        # 让狗玩耍
        dog.game()


# 1.创建 狗 对象
# wangcai = Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")

# 2.创建一个 小明 对象
xiaoming = Person("小明")

# 3.让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)