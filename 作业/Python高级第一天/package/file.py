"""
文件操作模块有以下功能(写在类里面的函数)：
    读取文件内容
    写入内容到文件中
    复制文件
    删除文件
    文件改名
"""
# 导入shutil模块
import shutil
# 导入os模块
import os
# 创建一个文件操作类
class FileTool(object):
    # 读取文件内容
    def read(self,path):
        # 打开文件
        fp = open(path,"r",encoding="utf8")
        # 读取文件
        data = fp.read()
        # 关闭文件
        fp.close()
        # 返回读取到的数据
        return data
    # 写入内容到文件
    def write(self,path,data):
        # 打开文件
        fp = open(path, "w", encoding="utf8")
        # 写入内容到文件,覆盖写
        fp.write(data)
        # 关闭文件
        fp.close()
    # 复制文件
    def copy(self,source,target):
        shutil.copyfile(source,target)
    # 删除文件
    def delete(self,path):
        os.remove(path)
    # 文件改名
    def rename(self,path,name):
        shutil.move(path,name)

if __name__ == '__main__':
    # print(FileTool().read("dir.py"))
    # FileTool().write("test.py","测试")
    # FileTool().copy("test.py","test_new.py")
    # FileTool().delete("test_new.py")
    FileTool().rename("test.py","test_new.txt")