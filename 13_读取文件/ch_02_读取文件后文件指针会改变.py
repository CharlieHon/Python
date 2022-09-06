# 1.打开文件
file = open("README")

# 2.读取文件内容
text = file.read()
print(text)
print(len(text))    # 48
print("-" * 50)

text = file.read()
print(text)
print(len(text))    # 0 文件指针移动到读取内容的末尾，读取不到内容了

# 3.关闭文件
file.close()