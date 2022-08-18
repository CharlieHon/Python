"""
1. 定义布尔型变量 `has_ticket` 表示是否有车票
2. 定义整型变量 `knife_length` 表示到的长度，单位：厘米
3. 首先检测是否有车票，如果有，才允许进行 案件
4. 安检时，需要检查刀的长度，判断是都超过20厘米

	- 如果超过20厘米，提示刀的长度，不允许上车
	- 如果不超过，安检通过
5. 如果没有车票，不允许进入
"""
has_ticket = True
knife_length = 15
if has_ticket:
    print("车票检查通过，准备开始安检")
    if knife_length <= 20:
        print("安检通过，祝您旅途愉快")
    else:
        print("携带道具长度为 %d厘米" % knife_length)
        print("不允许上车")
else:
    print("请先买票！")