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
        # 1.针对子类特有的需求，编写代码
        print("神犬吠叫")

        # 2.使用 super(). 调用原本在父类中封装的方法
        super().bark()
        
        # 父类名.方法(self) 调用父类方法，效果同上，但不推荐使用
        # Dog.bark(self)
        
        # 3.增加其他子类的代码
        print("恶龙咆哮")



xtq = XiaoTianQuan()

# 如果子类中，重写了父类的方法
# 再使用子类对象调用方法时，会调用子类中重写的方法
xtq.bark()