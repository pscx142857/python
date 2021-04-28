"""
    打包:
        写的位置是在形参,但是针对的是实参
            针对的是传入的实参的个数不确定
        def 函数名(*args):
            * 表示打包,将传入的所有的位置参数,打包成元组 -->args
        def 函数名(**kwargs):
            ** 表示打包,将传入的所有的关键字参数打包成字典 -->kwargs
"""

def sum(*args):
    """
    计算任意个数的和
    :param args: 传入的任意个数的位置参数,组成的元组
    :return: 任意个数的和
    """
    sm = 0
    for i in args:
        sm += i
    return sm

print(sum(1,2,3,4))

# 自我介绍
def show(name,age,**kwargs):
    """
    自我介绍,爱好不止一个
    :param name: 姓名
    :param age: 年龄
    :param kwargs: 将关键字参数打包成的字典
    :return:
    """
    print("我的名字是:",name)
    print("我的年龄是:",age)
    print("我的爱好是:",kwargs)

show("彭胜",18,p1 = "女",p2 = "么么哒")


def su(*tum):
    """
    计算任意个数的和
    :param tum: 传入的任意个数的位置参数,组成的元组
    :return: 任意个数的和
    """
    sm = 0
    for i in tum:
        sm += i
    return sm

print(su(1,2,3,4))