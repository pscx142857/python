# 添加或者修改,如果键不存在,就增加,如果存在,就修改值
dic = {"name":"张三","age":22,"中文":"试试"}
dic["name"] = "王五"
dic["height"] = 99
print(dic)
# 不存在时,添加键值,存在时,返回值
a = dic.setdefault("name2","赵四")
b = dic.setdefault("name","张三") # 不管存不存在都会返回现在的value
print(a)
print(b)
# 合并,如果已有内容则会覆盖掉
dic1 = {"name":"张飞","hight":200}
dic2 = {"name":"赵云","age":22}
dic1.update(dic2)
print(dic1)
# 根据key来删除键值,如果key不存在,则会报错
#del dic1["aaa"] #KeyError: 'aaa'
del dic1["hight"]
print(dic1)
# 根据键来删除,并返回value的值,如果不存在,则会报错
v = dic1.pop("name")
print(v)
# 清空字典
dic3 = {"name":"张飞","hight":200}
dic3.clear()
print(dic3)
# 查询
dic4 = {"name":"张飞","hight":200}
print(dic4["name"]) #根据键来查询,如果key不存在,则会报错
print(dic4.get("aaa")) #根据键来查询,如果key不存在,则返回None
# 获取键值对的数量(长度)
print(len(dic4))
# 获取字典中所有的值
a = dic4.values()
print(type(a))
print(list(a)) #转换成list
# 获取字典中所有的键
b = dic4.keys()
print(type(b))
print(list(b))
# 判断键是否在字典中存在,返回一个bool类型的值
print("name" in dic4)