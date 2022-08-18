age = int(input("请输入年龄："))
if age >= 0 and age <= 120:
    print("legal")

python_score = int(input("Python成绩: "))
c_score = int(input("C语言成绩: "))
if python_score >= 60 or c_score > 60:
    print("pass")

is_employee = bool(input("是否是本公司员工: "))
if is_employee:
    print("Welcome!")
else:
    print("Worn!")