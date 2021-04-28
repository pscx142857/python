"""
    操作文件:
        读:
            fp.read()       # 读取文件中所有的内容
            fp.readline()   # 读取下一行的内容
            fp.readlines()  # 按行读取完,读取出来的是列表,列表里面的元素就是一行的内容
        写:
            fp.write("内容") # 将内容写入到文件
            fp.writelines(列表) # 将列表中的元素写入到文件中
    关闭文件:
        fp.close()
"""
# 打开文件
fp = open("test.txt","r",encoding="utf8")
# 操作文件
# data = fp.read() # 读取所有的内容
# data = fp.readline() # 读取下一行的内容
# data = fp.readline() # 读取下一行的内容
data = fp.readlines() # 按行读取完,得到一个列表
# 关闭文件
fp.close()
print(data)

# 打开文件
fg = open("test.txt","w",encoding="utf8")
# 操作文件
# fg.write("w是覆盖写")
ls = ["我是第一个\n","我是第二个"]
fg.writelines(ls) # 将一个列表写入
# 关闭文件
fg.close()