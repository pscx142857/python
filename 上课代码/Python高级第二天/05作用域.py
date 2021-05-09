"""

"""
# 全局作用域
name = "张三"
def info():
    # 局部作用域
    age = 18
# 内建作用域
print("name")

def wai():
    sex = "男" # 闭包变量,闭包作用域
    def nei():
        print(sex)
    nei()

wai()
