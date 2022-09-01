def print_info(name, title="学生", gender=True):

    """
    :param title:职位
    :param name:姓名
    :param gender: True 男生 False 女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("[%s]%s 是 %s" % (title, name, gender_text))


# 假设班上的同学，男生居多，所以将默认值设置为男生
# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
print_info("小明")
print_info("小红",gender=False)