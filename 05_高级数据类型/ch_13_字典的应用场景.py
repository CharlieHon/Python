# 使用多个键值对，存储描述一个 `物体` 的相关信息--描述更复杂的数据信息
# 将多个字典放在一个列表中，再进行遍历，在循环体内部针对每一个字典进行相同的处理
card_list = [
    {"name":"xiaoming",
    "qq":"123456",
    "phone":"10086"},
    {"name":"zhangsan",
    "qq":"456789",
    "phone":"10010"}
]

for card_info in card_list:
    print(card_info)