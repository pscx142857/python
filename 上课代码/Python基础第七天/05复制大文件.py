# 打开文件
fp = open("user.txt","rb")
fp_new = open("user-副本.txt","wb")
# 操作文件
data = fp.read(1) # 先读取一份数据
while data:
    fp_new.write(data)
    data = fp.read(1) # 读取第二份数据
# 关闭文件
fp.close()
fp_new.close()