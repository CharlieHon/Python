# 无限循环，由用户决定何时结束
import cards_tools
while True:

    # 显示功能菜单
    cards_tools.show_menu()

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是 【%s】" % action_str)

    # 1,2,3 针对名片的操作
    if action_str in ["1", "2", "3"]:
        # 如果在程序开发时，不希望立刻编写分支内部的代码
        # 可以使用 pass 关键字，表示一个占位符，能够保证程序结构正确！
        # 程序运行时，pass 关键字不会执行任何的操作

        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
        # 查询名片
        else:
            cards_tools.search_card()
    # 0 退出系统
    elif action_str == "0":
        print("-" * 50)
        print("退出系统")
        print("欢迎再次使用【名片管理系统】")
        # pass
        break
    # 其他内容输入错误，提示用户
    else:
        print("您输入的不正确，请重新选择")
