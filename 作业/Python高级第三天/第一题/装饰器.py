"""
装饰器:
    在不修改原来函数代码的基础上,可以增加一些功能
"""
# 定义装饰器函数,让原始函数可以飞
def decorator(f):
    def info():
        f()
        print("我现在可以起飞了")
    return info # 返回的是info的内存地址

# 原始函数,只会跑
@decorator # 语法糖,直接@装饰器函数名
def show():
    print("我只会跑")

# 函数名直接调用
show()