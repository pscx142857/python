"""
    匿名函数:
        变量 = lambda 形参1,形参2...:函数体
    就一行代码,所以函数体都比较简单
    默认有返回计算的结果
    通常作为参数传递给普通函数的使用
"""
# 匿名函数计算两个数的和
sum = lambda a,b:a+b
# 函数名调用
print(sum(5,9))

# 两个数的任意算法
def cc(a,b,op):
    return op(a,b)
# 计算两个数的积
s = cc(5,6,lambda a,b:a*b)
print(s)
# 计算两个数的和
s = cc(7,6,lambda a,b:a+b)
print(s)
# 计算两个数的商
s = cc(12,6,lambda a,b:a/b)
print(s)

"""
    打包:
        打包位置参数,def 函数名(*args):
                        函数体
        打包关键字参数,def 函数名(**kwargs):
                        函数体
"""
# 计算任意个数的和
def sum(*args):
    j = 0
    for i in args:
        j += i
    return j
# 调用时会打包成元组-->args
print(sum(1,5,6))
# 自我介绍时,说出自己的爱好,不限
def show(**kwargs):
    print(f"我的爱好是:{kwargs}")
show(k1 = "吃饭",k2 = "睡觉")
"""
    拆包:
        拆包元组和列表
            函数名(*li)
            函数名(*tup)
        拆包字典
            函数名(**dic)
"""
def sum_3(a,b,c):
    """
    计算3个数的和
    :param a: 第一个求和数
    :param b: 第二个求和数
    :param c: 第三个求和数
    :return: 返回三个数的和
    """
    return a+b+c
ls = [5,7,9]
# *ls拆包列表,列表元素个数和形参个数一一对应
print(sum_3(*ls))

tup = (7,3,10)
# *tup拆包元组,列表元素个数和形参个数一一对应
print(sum_3(*tup))

dic = {"a":5,"b":5,"c":5}
# **dic拆包字典,键和形参对应
print(sum_3(**dic))

"""
    变量的作用域
        全局变量
            定义在函数的外面,所有地方都可以用
        局部变量
            定义在函数的里面,只能在函数内使用,不能在函数外使用
            函数内要修改全局变量,用global引入
"""
name = "张三"
def xixi():
    # global 引入全局变量,可以在函数内部修改
    global name
    name = "李四"
    age = 18
    print("我的年龄是",age)
# age是局部变量,函数外面不能使用
# print(age) # NameError: name 'age' is not defined
# 调用函数才会执行函数内部的代码
xixi()
print(name) # 李四
"""
    文件的操作
        # 打开文件
            open("路径","打开方式","编码")
            相对路径:以./开头,当前目录,可以不写 或者../上级目录
            绝对路径:以根目录开头/或者\
            打开方式:
                r 只读的方式打开文本文件
                w 覆盖写的方式打开文本文件,文件不存在的情况下会创建文件
                a 追加写的方式打开文本文件,文件不存在的情况下会创建文件
                
                rb 只读的方式打开二进制文件
                wb 覆盖写的方式打开二进制文件,文件不存在的情况下会创建文件
                ab 追加写的方式打开二进制文件,文件不存在的情况下会创建文件
        # 操作文件
            read() 全部读
            readline() 读取下一行
            readlines() 一行一行读,存在列表中
            
            write() 写入
            writelines() 将列表中的元素写入
        # 关闭文件
            close()
"""
# 打开文件
fp = open("test.txt","w",encoding="utf8")
# 操作文件
fp.write("覆盖写")
# 关闭文件
fp.close()

# 打开文件
fp = open("test.txt","a",encoding="utf8")
# 操作文件
ls = ["第一句话","第二句话"]
fp.writelines(ls)
# 关闭文件
fp.close()

# 打开文件
fp = open("test.txt","r",encoding="utf8")
# 操作文件
# data = fp.read() 读取全部内容
# data = fp.readline() 读取下一行
data = fp.readlines() # 按行读取,装到一个列表里

print(data)
# 关闭文件
fp.close()