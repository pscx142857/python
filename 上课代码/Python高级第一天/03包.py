"""
    包:带__init__文件的目录
    导入:
        import一定要到模块,因为代码是放在模块中的
        import 包名.模块名
        from 包名 import 模块名
        from 包名.模块名 import 变量|函数|类
        from 包名.模块名 import *
    使用:
"""
# import 包名.模块名
# import package.module
# print(package.module.name)
# from 包名 import 模块名
# from package import module
# print(module.name)
# from 包名.模块名 import 变量 | 函数 | 类
# from package.module import name
# print(name)
# from 包名.模块名 import *
from package.module import *
print(name)