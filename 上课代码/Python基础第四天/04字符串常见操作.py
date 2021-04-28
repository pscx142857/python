# strip去除空格
name = "  两边有两个空格  "
str = name.strip()
print("--"+str+"--") #去除两边的空格,无论几个都可以去除
print("--"+name.rstrip()+"--") # 去除右边的空格
print("--"+name.lstrip()+"--") # 去除左边的空格

# split 分割
name = "我是第一个 我是第二个 我是第三个"
ls = name.split() # 默认按照空格进行分割
print(ls)
name = "我是第一个,我是第二个,我是第三个"
ls = name.split(",") # 按照指定的符号进行分割
print(ls)
ls = name.split(",",1) # 后面的1表示分割几次
print(ls) #['我是第一个', '我是第二个,我是第三个']
ls = name.rsplit(",",1) # 从后面开始进行分割,
print(ls) # ['我是第一个,我是第二个', '我是第三个']
# 大小写转换
name = "tony"
print(name.upper()) #转换成大写
name = "TONY"
print(name.lower()) #转换成小写
# 判断开头结尾
name = "tony.avi"
print(name.startswith("t")) # 判断以什么开头,返回一个bool值
print(name.endswith(".avi")) # 判断以什么结尾,返回一个bool值
# 字符串格式化函数
print("我的名字是{},我的名字是{},我的名字是{}".format("张三","李四","王五")) #
print("我的名字是{0},我的名字是{1},我的名字是{0}".format("张三","李四","王五")) # 根据索引来格式化
# 关键字函数传入
print("我的名字是{name},我的名字是{name1},我的名字是{name2}".format(name="张三",name1="李四",name2="王五"))
# 使用字符串连接列表之间的元素
ls = ["1","2","3"]
s = "-"
print(s.join(ls))
# 替换
str = "aaaabbbccc"
print(str.replace("aa","B",1))
# 判断字符串是否由纯数字组成
print(str.isdigit())
str = "131254845"
print(str.isdigit())