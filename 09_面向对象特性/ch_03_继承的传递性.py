class Animal:

    def eat(self):
        print("吃")
    
    def drink(self):
        print("喝")
    
    def run(self):
        print("跑")
    
    def sleep(self):
        print("睡")


class Dog(Animal):

    def bark(self):
        print("犬吠")


class xiaotianquan(Dog):

    def fly(self):
        print("哮天犬会飞")


# 创建一个哮天犬的对象
xtq = xiaotianquan()

xtq.fly()
xtq.bark()
xtq.eat()