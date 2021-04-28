# 写代码，有如下变量，请按照要求实现每个功能
#     name = "posekakaka"
#     a. 移除name 变量对应的值两边的空格，并输出移除后的内容
#     b. 判断name 变量对应的值是否以 "po" 开头，并输出结果
#     c. 判断name 变量对应的值是否以 "a" 结尾，并输出结果
#     d. 将name 变量对应的值中的 “k” 替换为 “c”，并输出结果
#     e. 将name 变量对应的值根据 “k” 分割，并输出结果。
#     f. 请问，上一题 e 分割之后得到值是什么类型（可选）
name = "posekakaka"
# a. 移除name 变量对应的值两边的空格，并输出移除后的内容
print(name.strip())
# b. 判断name 变量对应的值是否以 "po" 开头，并输出结果
print(name.startswith("po"))
# c. 判断name 变量对应的值是否以 "a" 结尾，并输出结果
print(name.endswith("a"))
# d. 将name 变量对应的值中的 “k” 替换为 “c”，并输出结果
print(name.replace("k","c"))
# e. 将name 变量对应的值根据 “k” 分割，并输出结果。
print(name.split("k"))
# f. 请问，上一题 e 分割之后得到值是什么类型（可选）
ls = name.split("k")
print(type(ls))  #<class 'list'>