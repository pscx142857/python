"""
    将user.txt复制一份,文件名为user-副本.txt
"""

filename = input("请输入要复制文件:")
num = filename.rindex(".")
new_filename = filename[:num:]+"-副本"+filename[num::]
# print(new_filename)
# 打开文件
fp = open(filename,"r",encoding="utf8")
new_file = open(new_filename,"w",encoding="utf8")
# 操作文件
"""
    读取所有复制,读取出来是字符串
# 将源文件的内容读出来
data = fp.read()
# 将读出来的内容写入到目标文件里
new_file.write(data)
"""
"""
    按行读取复制,读取出来是列表
"""
# 将源文件的内容读出来,按行读取
data = fp.readlines()
# 将内容写入到目标文件,按行写
new_file.writelines(data)
# 关闭文件
fp.close()
new_file.close()
