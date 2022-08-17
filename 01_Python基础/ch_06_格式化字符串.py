"""
1. 定义字符串变量`name`，输出 我的名字叫小明，请多多关照！
2. 定义整数 变量`student_no`，输出 我的学号是 000001
3. 定义小数`price`、`weight`、`money`输出 苹果单价 9.00元/斤， 购买了5.00斤， 需要支付45.00元
4. 定义一个小数 `scale` ，输出 数据比例是 10.00%
"""
name = "小明"
print("我的名字叫 %s ，请多多关照！" % name)

student_no = 100
print("我的学号是 %06d" % student_no)

price = 9.00
weight = 5.00
money = price * weight
print("苹果单价 %.2f元/斤， 购买了%.3f斤， 需要支付%.4f元" % (price, weight, money))

scale = 0.25
print("数据比例是 %.2f%%" % (scale * 100))