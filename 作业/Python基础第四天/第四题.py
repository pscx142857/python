# 写代码，有如下字典，请按要求实现每个功能
#     dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
#     a. 请循环输出所有的key
#     b. 请循环输出所有的value
#     c. 请循环输出所有的key 和value
#     d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
#     e. 请在修改字典中 “k1” 对应的值为 “itsouce”，输出修改后的字典
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# a. 请循环输出所有的key
# 方法一:
for key in dic:
    print(key)
# 方法二:
for i in list(dic.keys()):
    print(i)
# b. 请循环输出所有的value
# 方法一:
for key in dic:
    print(dic[key])
# 方法二:
for i in list(dic.values()):
    print(i)
# c. 请循环输出所有的key 和value
for k,v in dic.items():
    print("key:",k)
    print("value:",v)
# d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
#方法一:
dic["k4"] = "v4"
print(dic)
#方法二:
dic.setdefault("k4","v4")
print(dic)
# e. 请在修改字典中 “k1” 对应的值为 “itsouce”，输出修改后的字典
dic["k1"] = "itsouce"
print(dic)