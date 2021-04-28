# 转义字符\n和\t代表什么，如何在字符串中放入一个反斜线字符\
str = "1122\n33" # \n 表示换行
print(str)
str = "1122\t33" # \t 表示tab
print(str)
str = "1122\\33" # \\就可以放入一个反斜线
print(str)