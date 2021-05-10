"""
装饰器:在不修改原函数代码的情况下,增加新的功能
"""

def show_2():
    print("小羊羊")

# 函数名作为参数传入,传入什么就调用什么函数
def factory(f):
    def info():
        print("**************************")
        f()
        print("**************************")
    return info # 将info函数的内存地址返回
@factory  # 相当于 show_1 = factory(show_1)
def show_1():
    print("小马马")

# 想实现修改原来的函数,就实现装饰器效果
# show_1 = factory(show_1) # 得到info函数的内存地址,赋值给show_1
show_1()
show_1()
show_1()
show_1()
show_1()