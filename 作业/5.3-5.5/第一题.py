"""
1. 将 字符串 列表 字典的课件中的相关语法敲一遍
"""
"""
字符串:
    里面存储的是字符类型的不可变有序的容器
"""
# 转义字符\,可以将有意义的字符转成无意义的字符,也可以将无意义的字符转换成有意义的字符
# 无意义-->有意义
print("这是两个空格\t哦")
print("这是一个回车\n哦")
# 有意义-->无意义
print("这两个引号\"\"无意义了哦")
# 根据索引取值
st = "零一二三四五六七八九十"
print(st[0]) # 零
# 切片,取出部分字符
st_new = st[1:5:1]
print(st_new)
# while遍历字符
i = 0
while i < len(st):
    print(st[i])
    i += 1
# for in 专业遍历
for j in st:
    print(j)
# 去除左右两边空格
st = "  两边都有  "
st_new = st.strip()
print(st_new)
# 去除左边空格
st_new = st.lstrip()
print(st_new)
# 去除右边空格
st_new = st.rstrip()
print(st_new)
# 字符串分割
st = "1,2,3,4,5"
ls = st.split(",")
print(ls)
# 大写-->小写
st = "SoS"
print(st.lower())
# 小写-->大写
st = "sos"
print(st.upper())
# 判断是否以什么字符开头
print(st.startswith("s"))
# 判断是否以什么字符结尾
print(st.endswith("p"))
# 字符串连接
ls = ["1","2","3","4","5"]
print("--".join(ls))
# 字符串替换
st = "你是sb吗"
print(st.replace("sb","**"))
# 判断是否全部是数字组成
print(st.isdigit())
"""
字典:
无序,可变的容器,键值对组成
键唯一,值不唯一
"""
# 添加或者修改
dic = {"name":"张三","age":"18"}
# 根据键来修改
dic["name"] = "李四"
# 没有就会自动添加
dic["sex"] = "女"
print(dic)
# 添加或者返回原值
# 键存在则不修改,返回原来的值
v1 = dic.setdefault("name","王五")
# 键不存在,则添加,并返回值
v2 = dic.setdefault("height","500")
print(v1)
print(v2)
print(dic)
# 合并,如果存在就覆盖,如果不存在就添加
dic1 = {"name":"张三","age":"18"}
dic2 = {"name":"李四","sex":"女"}
dic1.update(dic2)
print(dic1)
# 删除
dic = {"name":"张三","age":"18"}
# 根据键来删除,如果键不存在会报错
del dic["name"]
print(dic)
# 根据键来删除,会返回删除的值,如果键不存在会报错
dic = {"name":"张三","age":"18"}
v = dic.pop("age")
print(v)
print(dic)
# 清空字典
dic = {"name":"张三","age":"18"}
dic.clear()
print(dic)
# 根据键来查询
dic = {"name":"张三","age":"18"}
# 如果键不存在,就会报错
print(dic["name"])
# 如果键不存在,返回None
print(dic.get("age"))
# 获取字典的键值对数量(长度)
print(len(dic))
# 获取字典中所有的值
print(list(dic.values()))
# 获取字典中所有的键
print(list(dic.keys()))
# 判断键是否在字典中存在
print("name" in dic)
# 遍历key
for key in dic:
    print(key)
# 遍历value
for value in dic.values():
    print(value)
# 遍历键值对
for item in dic.items():
    print(item)
# 遍历键和值
for key,value in dic.items():
    print(key)
    print(value)
"""
列表:
    有序的,可变的,数据容器
"""
# 追加,追加到最后
ls = ["a","b","c"]
ls.append("d")
print(ls)
# 插入,根据索引插入
ls.insert(0,"1")
print(ls)
# 扩展
ls1 = ["a","b","c"]
ls2 = ["d","e","f"]
# 将列表2的数据追加到列表1后面
ls1.extend(ls2)
print(ls1)
# 删除
ls = ["a","b","c"]
# 删除指定索引的数据
del ls[0]
print(ls)
# 删除第一个出现的指定数据
ls = ["a","b","c"]
ls.remove("b")
print(ls)
# 弹出末尾的数据
ls = ["a","b","c"]
st = ls.pop()
print(st)
print(ls)
# 弹出指定索引的数据
ls = ["a","b","c"]
st = ls.pop(0)
print(st)
print(ls)
# 清空列表
ls = ["a","b","c"]
ls.clear()
print(ls)
# 查询指定索引的数据
ls = ["a","b","c","d","e","f"]
print(ls[1])
# 切片
ls_new = ls[0:4:1]
print(ls_new)
# 查询数据第一次出现时的索引
print(ls.index("c"))
# 查询列表长度
print(len(ls))
# 查询数据在列表中出现的次数
print(ls.count("c"))
# 修改列表的元素
ls[0] = "A"
print(ls)
# 升序
ls = [1,2,4,0]
ls.sort()
print(ls)
# 降序
ls.sort(reverse=True)
print(ls)
# 反转
ls = ["a","b","c"]
ls.reverse()
print(ls)
# 列表遍历
# while遍历
i = 0
ls = ["a","b","c"]
while i < len(ls):
    print(ls[i])
    i += 1
# for专业遍历
for j in ls:
    print(j)
# 列表嵌套
ls = [["a","b"],["c","d"]]
print(ls[0])