class Dog:

    @staticmethod
    def run():
        # 不访问实例属性/类属性
        print("小狗要跑...")

    def __init__(self, name) -> None:
        
        self.name = name

# 通过 类名. 调用静态方法 -- 不需要创建对象，就可以调用
Dog.run()