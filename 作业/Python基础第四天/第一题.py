"""
    元组: 有序的,不可变的,容器
    怎么定义一个单元组,两种方式
    可以给多个变量赋值
"""
#定义一个元组
tup = (1,2,3,5)
#先定义一个单元素列表,转换成元组
ls = ["我是一个单元组"]
tup = tuple(ls)
print(tup)
#直接定义单元素元组
tup1 = (2,)
print(tup1)
#给多个变量赋值
tup = ("第一个值","第二个值")
a,b = tup
print(a,b)
"""
    转义符\
"""
# 将有意义的字符转换成没有意义的字符
st = "我很\"帅\"的"
print(st)
st2 = "C:\\安装目录"
print(st2)
# 将没有意义的字符转换成有意义的字符
st = "大家注意我要\n换行了"
st2 = "大家注意我要\t向后空两格了"
print(st)
print(st2)
"""
    字符串:不可变,有序的,存放字符的容器
"""
#去除左右两边的空格或者指定字符
st = "  有两个空格  "
new_st = st.strip()
print(new_st)
st2 = "==把这个等号去掉--"
new_st = st2.strip("=")
print(new_st)
#去掉左边的
new_st = st2.lstrip("=")
print(new_st)
#去掉右边的
new_st = st2.rstrip("-")
print(new_st)
#将字符串分割成列表
st = "a,b,bc,d"
new_st = st.split(",")
print(new_st)
#将列表连接成字符串
ls = ['a', 'b', 'bc', 'd']
st = "--".join(ls)
print(st)
#大小写转换
name = "tony"
print(name.upper())
name = "TONY"
print(name.lower())
#判断字符是否以什么开头
st = "pps.jpg"
print(st.startswith("pp"))
#判断字符是否以什么结尾
print(st.endswith(".jpg"))
#替换
new_st = st.replace("pp","bb")
print(new_st)
#判断字符是否是纯数字
print(st.isdigit())
"""
    字典:无序的,可变的,容器
    由键值对组成,逗号隔开
    键唯一,值可以不唯一
    键的类型一般为不可变的,字符串较多.值任意
"""
#增加或者修改
dic = {"name":"兮兮","age":99}
dic["name"] = "丫丫"
dic["height"] = 88
print(dic)
#增加或者返回原来的值
st = dic.setdefault("name","露露")
st2 = dic.setdefault("job","空姐")
print(st)
print(st2)
print(dic)
#合并
dic1 = {"name":"第一个","age":99}
dic2 = {"name":"第二个","heigh":9}
dic1.update(dic2)
print(dic1)
#删除
dic3 = {"name": "莉莉", "tel": "13125018132", "company": "源码时代", "job": "秘书", "address": "天府新谷"}
del dic3["name"]
st = dic3.pop("tel")
print(st)
print(dic3)
dic3.clear()
print(dic3)
#查询
dic4 = {"name": "莉莉", "tel": "13125018132", "company": "源码时代", "job": "秘书", "address": "天府新谷"}
print(dic4["name"])
print(dic4.get("name"))
print(dic4.get("36"))
#获取所有的键
for k in dic4.keys():
    print(k)
#获取所有的值
for v in dic4.values():
    print(v)
#查询有多少键值对
print(len(dic4))
#遍历
for k,v in dic4.items():
    print(k,v)
"""
    无序的,不可重复的,可变的
"""
st = {999,777,888,999}
print(st)
# 去重
ls = [777,888,999,777,444,888]
print(list(set(ls)))
"""
    for循环
"""
for i in range(1,10):
    print(i)
    # if i == 6:
    #     break 如果break执行了,那么else里面的不再执行
else:
    print("已经循环完毕")