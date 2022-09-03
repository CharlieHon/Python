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


class XiaoTianQuan(Dog):

    def fly(self):
        print("哮天犬会飞")

    def bark(self):
        print("神犬吠叫")



xtq = XiaoTianQuan()

# 如果子类中，重写了父类的方法
# 再使用子类对象调用方法时，会调用子类中重写的方法
xtq.bark()