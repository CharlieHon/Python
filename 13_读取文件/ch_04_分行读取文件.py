# 1.打开文件
file = open("README")

# 2.读取文件
while True:
    # 每次读取一行
    text = file.readline()
    
    # 判断是否读取到内容
    if not text:
        break
    
    print(text, end="")

# 关闭文件
file.close()