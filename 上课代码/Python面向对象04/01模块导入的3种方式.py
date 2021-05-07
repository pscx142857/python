"""
    导入:
        第一种:import 模块名 导入模块里面的所有
        第二种:from 模块名 import 变量名|函数名|类名 导入指定的变量|函数|类
        第三章:from 模块名 import * 导入模块里面的所有
    使用:
        import 后面跟什么就用什么,用面向对象的语法.
    别名:
        可以给导入的东西取一个别名,用as
            例:import 模块名 as 别名
                from 模块名 import 变量名|函数名|类名 as 别名
"""
# 第一种,import 模块名
# import module
#
# print(module.name)
# 第二种,from 模块名 import 变量|函数|类
# from module import name
# print(name)
# 第三种,from 模块名 import *
from module import *
print(name)
