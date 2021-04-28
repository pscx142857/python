# 打开文件
fp = open("图片.ico","rb") # 以二进制的方式读取
new_fp = open("图片-副本.ico","wb") # 以二进制的方式写入
# 操作文件
# 读取原文件数据,以二进制的方式
data = fp.read()
# 写入到目标文件
new_fp.write(data)
# 关闭文件
fp.close()
new_fp.close()