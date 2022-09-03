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



class Cat(Animal):

    def catch(self):
        print("抓老鼠")


# 创建一个哮天犬的对象
xtq = xiaotianquan()

xtq.fly()
xtq.bark()
xtq.eat()

# 哮天犬 和 Cat 之间没有继承关系，不能调用 catch()
# xtq.catch()