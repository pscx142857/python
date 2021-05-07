"""
目录操作模块有以下功能：
    创建目录
    删除目录（空目录或非空目录）
    查找目录中是否存在某个文件
"""
# 导入os模块
import os
# 定义一个目录操作类
class DirTool(object):
    # 创建目录
    def makedir(self,path):
        os.mkdir(path)
    # 删除目录
    def deletedir(self,path):
        os.removedirs(path)
    # 查找目录中是否存在某个文件
    def isfile(self,path):
        return os.path.exists(path)

# 模块中自我测试
if __name__ == '__main__':
    DirTool().makedir("test")
    DirTool().deletedir("test1")
    print(DirTool().isfile("file.py"))
