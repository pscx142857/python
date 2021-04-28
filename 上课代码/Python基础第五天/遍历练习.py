"""
    emp = [
    {"name": "小乔", "age": 18, "sex": "女"},
    {"name": "大乔", "age": 20, "sex": "女"},
    {"name": "张飞", "age": 30, "sex": "男"},
    {"name": "关羽", "age": 34, "sex": "男"},
    {"name": "貂蝉", "age": 17, "sex": "女"},
    {"name": "吕布", "age": 26, "sex": "男"},
]

# 要求 获取 员工表中 是女生 并且年龄 小于等于18的 员工姓名

"""
emp = [
    {"name": "小乔", "age": 18, "sex": "女"},
    {"name": "大乔", "age": 20, "sex": "女"},
    {"name": "张飞", "age": 30, "sex": "男"},
    {"name": "关羽", "age": 34, "sex": "男"},
    {"name": "貂蝉", "age": 17, "sex": "女"},
    {"name": "吕布", "age": 26, "sex": "男"},
]
for i in emp:
    if i["sex"] == "女" and i["age"] <= 18:
        #print("女生:",i)
        print("人家是女生,我的年龄小于等于18,我的名字是:"+i["name"])