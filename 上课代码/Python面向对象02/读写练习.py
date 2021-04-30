# 打开文件
fp = open("test_练习.txt","r",encoding="utf8")
# 操作文件
data = fp.read()
ls = data.split(",")
# 关闭文件
fp.close()
print(ls)

ls[0] = "王五"
st = ",".join(ls)
fp = open("test_练习.txt","w",encoding="utf8")
fp.write(st)
fp.close()