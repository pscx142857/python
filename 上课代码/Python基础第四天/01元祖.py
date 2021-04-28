"""
    元祖的特殊用法(面试题)
"""
# 1,可以给多个变量赋值
tup = ("张三","李四")
a,b = tup
print(a)
print(b)
# 2,定义单元素元祖
# 方法一:将列表转换成元祖
tup = tuple(["张三"])
print(type(tup))
# 方法二
tup = ("张三",)
print(type(tup))

"""
    列表元祖之间的相互转换
"""
tup = ("张三","李四")
ls = list(tup)
print(type(ls))
new_tup = tuple(ls)
print(type(new_tup))