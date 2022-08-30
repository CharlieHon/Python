# 记录所有的名片字典
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用 【名片管理系统】V1.0")
    print()
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print()
    print("0. 退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")
    # 1.提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")

    # 2.使用用户输入的信息建立一个名片字典
    card_dict = {"name": name_str, "phone": phone_str,
                 "qq": qq_str, "email": email_str}

    # 3.及那个名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)

    # 4.提示用户添加成功
    print("添加 %s 的名片成功" % name_str)


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    # 判断是否存在名片记录，如果没有，提示用户且返回
    if len(card_list) == 0:
        print("当前名片没有任何记录，请使用新增功能添加名片！")
        # return 可以返回一个函数执行结果
        # 下方的代码不会被执行
        # 如果 return 后面没有任何的内容，表示会返回到调用函数的位置
        # 并且不会返回任何的结果
        return

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print()
    # 打印分隔线
    print("=" * 50)
    # 遍历名片列表依次输出字典信息
    for card_dict in card_list:
        # print(card_dict)
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"],
                                        card_dict["qq"], card_dict["email"]))


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")

    # 1.提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名：")
    # 2.遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"],
                                            card_dict["qq"], card_dict["email"]))

            # 针对找到的名片进行修改/删除操作
            deal_card(card_dict)

            break
    else:
        print("抱歉，没有找到 %s" % find_name)


def deal_card(find_dict):
    """处理查找到的名片"""
    action_str = input("请输入您想执行的操作"
                       "[1] 修改 [2] 删除 [3] 返回上级菜单：")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名【回车不修改】: ")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话【回车不修改】: ")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ号【回车不修改】: ")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱【回车不修改】: ")
        print("修改成功")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除成功")


def input_card_info(dict_value, tip_message):
    """修改名片信息
    :param dict_value: 字典中原有的值
    :param tip_message: 输入的提示信息
    :return: 如果用户输入了内容，就返回内容，否则返回字典中原有的值
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)
    # 2.针对用户的输入进行判断，如果用户输入内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3.如果用户没有输入内容，返回字典中原有的值
    else:
        return dict_value
