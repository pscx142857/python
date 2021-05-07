"""
模块和包的查找位置:
    1.内建位置:封装在python.exe里面
        例如:sys
    2.系统的标准位置:python的安装目录下的Lib目录下
        例如:os re random
    3.当前执行文件所在的目录 --> 右键run的py文件所在的目录
    4.三方包的存放路径 --> 从python的官方的三方包下载的包
        存放在:python的安装目录下的Lib目录下的site-packages目录中
    5.自定义的查找路径:
        1.import sys
        2.sys.path.append("路径")
"""
# sys模块中有一个path,path存放的就是模块和包的查找位置,是一个列表
import sys # 先导入sys模块
print(sys.path) # path中存放的是模块和包查找的位置
sys.path.append(r"C:\Users\Administrator\PycharmProjects\Python基础\上课代码\Python面向对象03预习") # 将自定义的路径添加到path中
print(sys.path)
import mod # 就可以导入自定义目录下的模块了
print(mod.a)