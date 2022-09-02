class Cat:

    def __init__(self, name):
        self.name = name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 走了" % self.name)

    def __str__(self):
        
        # 必须返回一个字符串
        return "我是小猫[%s]" % self.name

# tom 是一个全局变量，在程序执行结束时内存被释放
tom = Cat("Tom")
print(tom)