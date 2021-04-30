"""
6.定义一个文件操作类File，方法有：读取所有内容，读取数据按行返回，写入内容，追加数据。
    有以下方法：
        file.read(文件名)
        file.write(文件名,’内容’)
        file.readlines(文件名)
        file.append(文件名,’内容’)
"""
# 定义一个文件操作类
class FileTool(object):


    # 读取所有的内容
    def du(self,file):
        """
        根据传入的路径读取文件内容
        :param file: 文件路径
        :return: 返回读取到的所有内容,字符串类型
        """
        # 打开文件
        fp = open(file,"r",encoding="utf8")
        # 操作文件
        data = fp.read()
        # 关闭文件
        fp.close()
        return data
    # 读取数据按行返回
    def duhang(self,file):
        """
        根据传入的文件路径按行读取
        :param file: 文件的路径
        :return: 返回的是文件的内容,列表的形式,一个元素就是一行
        """
        # 打开文件
        fp = open(file, "r", encoding="utf8")
        # 操作文件
        data = fp.readlines()
        # 关闭文件
        fp.close()
        return data
    # 写入内容
    def xie(self,file,data):
        """
        根据传入的路径写入内容
        :param file: 要写入内容的文件路径
        :param data: 要写入的数据
        :return:
        """
        # 打开文件
        fp = open(file, "w", encoding="utf8")
        # 操作文件
        fp.write(data)
        # 关闭文件
        fp.close()
    # 追加数据
    def zhui(self,file,data):
        """
        根据传入的文件路径追加数据
        :param file: 文件的路径
        :param data: 要追加的数据
        :return:
        """
        # 打开文件
        fp = open(file, "a", encoding="utf8")
        # 操作文件
        fp.write(data)
        # 关闭文件
        fp.close()

# 创建一个文件操作对象
fl = FileTool()
# 调用读取所有内容的方法
print(fl.du("data_6.txt"))
# 调用按行读取
print(fl.duhang("data_6.txt"))
# 调用写入数据的方法
fl.xie("data_6.txt","看看写入了吗")
# 调用追加写入的方法
fl.zhui("data_6.txt","这是追加的")