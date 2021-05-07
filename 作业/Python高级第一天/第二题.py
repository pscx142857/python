"""
2.今天的上课代码实现一遍。
"""
"""
模块:
    一个py文件就是一个模块,标准模块中只存放变量,函数,类
    导入:
        import 模块名
        from 模块名 import 变量名|函数名|类
        from 模块名 import *
    使用:
        import后面跟什么就用什么.
"""
import module # import 模块名
print(module.name)
from module import info # from 模块名 import 变量名|函数名|类
info()
from module import *
print(name) #  from 模块名 import *
"""
包:
    存放模块的目录就是包,标准的包中有__init__.py文件
    导入:
        import 包名.模块名
        from 包名 import 模块名
        from 包名.模块名 import 变量名|函数名|类
        from 包名.模块名 import *
    使用:
        import后面跟什么就用什么.
"""
import package.modul_1 # import 包名.模块名

print(package.modul_1.name)
from package import modul_1 # from 包名 import 模块名

print(modul_1.name)
from package.modul_1 import show # from 包名.模块名 import 变量名|函数名|类
show()
from package.modul_1 import * # from 包名.模块名 import *
print(name)
"""
模块和包的查找位置
    内建位置:python.exe解析器中
    系统标准位置:python安装目录下的lib目录
    当前执行文件所在目录
    第三方包的存放目录:python安装目录下lib目录下的site-packages
    自定义的位置:
        import sys
        sys.path.append("路径")
查找顺序:内建位置-->系统标准位置-->当前所在位置-->第三方包存放位置-->自定义位置
"""
import sys
sys.path.append(r"C:\Users\Administrator\PycharmProjects\Python基础\上课代码\Python面向对象03预习")
import mod
print(mod.a)
"""
列表推导式:
    使用公式快速的生成一个列表
    语法:
        变量 = [表达式 for i in 容器 if 条件判断]
"""
ls = [i for i in range(1,10) if i % 3 == 0]
print(ls) # [3, 6, 9]
"""
随机数模块random
"""
import random
# 随机获取0到1之间的浮点数
print(random.random())
# 随机获取a到b之间的整数
print(random.randint(0, 9))
# 随机获取一个序列中的一个元素,序列:字符串,列表,元组
print(random.choice(ls))
# 随机获取一个序列中的指定个数元素
print(random.sample(ls,2))
"""
哈希散列:
    数据加密,常用于密码
    步骤:
        1.导入模块,import hashlib
        2.准备二进制数据
            直接读取文件,使用rb
            变量.encode("编码方式")
            b"字符串"
        3.实例化算法对象
            h = hashlib.md5(二进制数)
            h = hashlib.sha512(二进制数)
        4.获取16进制的加密数据
            h.hexdigest()
"""
# 导入hashlib模块
import hashlib
# 准备二进制数据
data = b"888888"
# 实例化算法对象
h = hashlib.md5(data)
# 获取加密后的数据
print(h.hexdigest())  # 21218cca77804d2ba1922c33e0151105