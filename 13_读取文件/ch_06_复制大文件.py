# 1.打开文件
file_read = open("README")
file_Write = open("README[复件]", "w")

# 2.读、写文件
while True:
    # 读取一行内容
    text = file_read.readline()

    # 判断是否读取到内容
    if not text:
        break
    file_Write.write(text)

# 3.关闭文件
file_read.close()
file_Write.close()