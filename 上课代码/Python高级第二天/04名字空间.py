"""
名字空间:变量名,函数名,类名的存放空间

全局名字空间:
    __name__:保存的是模块名,但是当前文件运行保存的就是main
    __file__:变量里面保存的就是当前文件的绝对路径
    __builtins__:保存的是内建名字空间里面的所有内容
    globals()
局部名字空间:
    locals()
内建名字空间:
    自己没有定义的,但是又能用的-->存放在内建名字空间中
"""
# 全局名字空间
name = "张三"
# 局部名字空间
def show():
    age = 18
    print("函数")
    l = locals()
    print(l)

show()
g = globals()
print(g)

print(dir(__builtins__))