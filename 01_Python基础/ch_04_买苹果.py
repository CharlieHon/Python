# 1.输入苹果的单价
price_str = input("苹果的单价：")
# 2.输入苹果的重量
weight_str = input("苹果的重量：")
# 3.计算支付的总金额
# 注意：两个字符串变量之间是不能直接用乘法的
# 将数据转换成小数，用小数来计算最终的金额
price = float(price_str)
weight = float(weight_str)
money = price * weight
print(money)