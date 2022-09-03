class Woman:

    def __init__(self, name) -> None:
        
        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d" % (self.name, self.__age))


a = Woman("小芳")

# 伪私有属性，在外界不能直接访问
print(a._Woman__age)

# 伪私有方法，同样不允许在外界直接访问
a._Woman__secret()

