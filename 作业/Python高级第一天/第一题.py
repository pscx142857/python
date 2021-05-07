"""
1.定义一个包
    包含两个模块：文件操作模块、目录操作模块
    文件操作模块有以下功能(写在类里面的函数)：
    读取文件内容
    写入内容到文件中
    复制文件
    删除文件
    文件改名
    目录操作模块有以下功能：
    创建目录
    删除目录（空目录或非空目录）
    查找目录中是否存在某个文件

"""
from package import file
from package import dir

# 读取文件内容
print(file.FileTool().read("作业.txt"))
# 写入内容到文件中
file.FileTool().write("test.txt","测试")
# 复制文件
file.FileTool().copy("test.txt","test_new.txt")
# 删除文件
file.FileTool().delete("test_new.txt")
# 文件改名
file.FileTool().rename("test.txt","test2.txt")
# 创建目录
dir.DirTool().makedir("test")
# 删除目录（空目录或非空目录）
dir.DirTool().deletedir("test")
# 查找目录中是否存在某个文件
print(dir.DirTool().isfile("test.txt"))
