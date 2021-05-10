"""
2.复习如何查看import路径查找信息，如何添加自定义目录作为路径查找信息；
    仿照课堂案例，实现可以import自定义模块（win： 在D盘mod目录下）
    import查找顺序如下:
    内建位置:python.exe解析器中
    系统位置:python安装目录下的lib目录
    当前文件执行的位置:当前py文件执行的目录
    第三方包安装的目录:python安全目录下的lib目录下的site-packages目录
    自定义的位置:自定义添加到sys.path列表中的位置
"""
# 导入sys模块
import sys
# 将自定义的目录添加到sys.path列表里面
sys.path.append(r"D:\mod")
import t
print(t.name)