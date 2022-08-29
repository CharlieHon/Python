# 要求：顺序并且居中对齐输出以下内容
poem = ["\n\t登鹳雀楼 ",
        "王之涣",
        "\t白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for p_str in poem:
    # 先使用 strip 方法去除字符串中的空白字符
    # 再使用 center 方法居中显示文本
    print("|%s|" % p_str.strip().center(10, "　"))
