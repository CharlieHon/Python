import re
from unicodedata import name


name_list = ["songjiang", "lujunyi", "wuyong", "gongsunsheng", "guansheng"]
num_list = [6, 8, 4, 1, 10]

# 升序
name_list.sort() # sort in place
num_list.sort()

# 降序
name_list.sort(reverse=True)    # 以降序的方式排序
num_list.sort(reverse=True)

# 逆序 (反转)
name_list.reverse()
num_list.reverse()

print(name_list)
print(num_list)