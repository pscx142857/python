"""
    函数的语法:
        def 函数名([形参1,形参2...]):
            函数体
            return 返回值
"""
def sum_2(a,b):
    c = a+b
    return c
"""
    函数的调用:
        函数名([实参1,实参2...])
"""
sum = sum_2(5,9)
print(sum)
# 注释加强
def sum_2(a,b):
    """
    求两数之和
    :param a: 第一个求和数
    :param b: 第二个求和数
    :return: 返回和的结果
    """
    c = a+b
    return c
# 参数加强
# 必传参数
def show(name,age):
    print(f"我的名字是:{name},我的年龄是:{age}")
# 默认参数
def show(name,age=18):
    print(f"我的名字是:{name},我的年龄是:{age}")
# 位置参数
show("张三",66)
# 关键字参数
show(age=19,name="张三")
# 返回值加强
# return可以不写,默认返回None
a = show("张三")
print(a)
# return一旦执行,函数终止
def pr():
    print("11111")
    return 2
    print("22222")
pr() # print("22222")将不再执行
# 可以有多个return
def big(a,b):
    if a > b:
        return a
    else:
        return b
big = big(9,10)
print(big)
# 一个return可以返回多个值,为一个元组
def fc():
    return 1,2,3,4
tup = fc()
print(tup) # (1, 2, 3, 4)