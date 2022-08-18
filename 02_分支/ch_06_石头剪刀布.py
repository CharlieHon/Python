"""
1. 从控制台输入要出的拳--石头(1)/剪刀(2)/布(3)
2. 电脑 **随机** 出拳--先假定电脑只会出石头，完成完整代码功能
3. 比较胜负
"""
# 导入随机工具包
# 在导入工具包时，应该将导入的语句，放在文件的顶部
# 因为，这样可以方便下方的代码，在任何需要的时候，使用工具包中的工具
import random
player = int(input("请输入您出的拳 石头(1)/剪刀(2)/布(3): "))
computer = random.randint(1, 3)
print("玩家出的拳头是 %d - 电脑出的拳是 %d" % (player, computer))
# 玩家胜利的三种情况
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3) 
        or (player == 3 and computer == 1)):
    print("玩家赢了！")
# 平局
elif player == computer:
    print("平居")
# 电脑获胜
else:
    print("电脑获胜！")