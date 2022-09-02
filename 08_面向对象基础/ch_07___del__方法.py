class Cat:

    def __init__(self, name):
        self.name = name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 走了" % self.name)


# tom 是一个全局变量，在程序执行结束时内存被释放
tom = Cat("Tom")
print(tom.name)

# del 关键字可以删除一个对象
del tom # 在分割线上方输出 __del__方法内容

print("-" * 50)