"""
列表推导式:通过一个公式,快速的生成一个列表
语法:
    变量 = [表达式 for i in 容器 if 条件判断]
    执行过程:
        首先从容器中依次遍历数据,每取一个数据,就到条件语句中进行判断
        条件不满足,这个数据就舍弃
        条件满足,将数据又带入到表达式中参与计算
    最终的计算结果,会添加到列表中

"""
# 将1-100的数字添加到列表
ls = []
for i in range(1, 101):
    ls.append(i)
print(ls)
# 用列表推导式实现
ls1 = [i for i in range(1, 101)]
print(ls1)
# 将1-100能被3整除的数添加到列表里
ls2 = [i for i in range(1, 101) if i % 3 == 0]
print(ls2)
# 得到1-100中能被3整除的数的平方的列表,结果:[9,36,81,...]
ls3 = [i**2 for i in range(1, 101) if i % 3 == 0]
print(ls3)

"""
emp = [
    {"name": "张飞", "age": 25, "sex": "男"},
    {"name": "张1", "age": 26, "sex": "女"},
    {"name": "张2", "age": 18, "sex": "男"},
    {"name": "张3", "age": 34, "sex": "女"},
    {"name": "张4", "age": 27, "sex": "男"},
    {"name": "张5", "age": 28, "sex": "女"},
    {"name": "张6", "age": 24, "sex": "女"},
    {"name": "张7", "age": 21, "sex": "男"},
    {"name": "张8", "age": 19, "sex": "女"},
]
# 使用列表推导式 得到 年龄大于20 性别为女 的姓名的列表
"""
emp = [
    {"name": "张飞", "age": 25, "sex": "男"},
    {"name": "张1", "age": 26, "sex": "女"},
    {"name": "张2", "age": 18, "sex": "男"},
    {"name": "张3", "age": 34, "sex": "女"},
    {"name": "张4", "age": 27, "sex": "男"},
    {"name": "张5", "age": 28, "sex": "女"},
    {"name": "张6", "age": 24, "sex": "女"},
    {"name": "张7", "age": 21, "sex": "男"},
    {"name": "张8", "age": 19, "sex": "女"},
]
# 使用列表推导式 得到 年龄大于20 性别为女 的姓名的列表
ls4 = []
for dic in emp:  # dic {'name': '张飞', 'age': 25, 'sex': '男'}
    if dic["age"] > 20 and dic["sex"] == "女":
        ls4.append(dic["name"])
print(ls4)

# 使用列表推导式的方式实现上面的需求
ls5 = [dic["name"] for dic in emp if dic["age"] > 20 and dic["sex"] == "女"]
print("----------------")
print(ls5)
