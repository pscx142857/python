# 全局变量定义在调用函数下面,是否能使用,不能
def show():
    print(name)
# name = "丫丫"
show()
name = "丫丫" # NameError: name 'name' is not defined