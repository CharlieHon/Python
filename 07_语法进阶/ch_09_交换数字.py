a = 6
b = 100

# 1.使用其他变量
c = a
a = b
b = c
print(a, b)

# 2.不使用其他的变量
a = a + b
b = a - b
a = a - b

print(a, b)

# 3. 利用元组，等号右边是一个元组，只是将小括号省略了
a, b = b, a
print(a, b)