"""
4.定义一个函数模块
    可以去除传入的字符串里面的所有空格,返回去除空格之后的字符串
"""
# 导入模块
import removespaces
# 定义一个有空格的字符串
st = " 1 2 3 4 5 6  7  8  "
# 调用模块中的函数,去除字符串中的空格
st_new = removespaces.stripspace(st)
print(st_new)