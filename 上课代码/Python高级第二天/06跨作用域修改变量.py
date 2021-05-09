"""

"""
# 全局变量
name = "张三"
def show():
    # 用global引入全局变量
    global name
    # 修改
    name = "李四"
    print(name)
# 调用执行
show()
print(name)

def wai():
    # 闭包变量
    age = 15
    def nei():
        # 用nonlocal引入闭包变量
        nonlocal age
        # 修改闭包变量
        age = 18
    nei()
    print(age)
wai()