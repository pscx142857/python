"""
6.定义一个函数,实现对字典的浅拷贝  分别使用copy（）和不使用
"""
import copy
# 使用copy的方式浅拷贝
def copy_self(dic):
    return copy.copy(dic)

dic = {"name":"张三","age":18}
dic_new = copy_self(dic)
print(dic_new) # {'name': '张三', 'age': 18}
# 修改原来的数据,查看是否修改了现在的数据
dic["name"] = "李四"
print(dic) # {'name': '李四', 'age': 18}
print(dic_new) # {'name': '张三', 'age': 18}

# 不使用copy,实现浅拷贝
def copy_dic(dic):
    dic_new = {}
    for k,v in dic.items():
        dic_new[k] = v
    return dic_new

dic1 = {"name":"兮兮","age":20}
dic2 = copy_dic(dic1)
print(dic2) # {'name': '兮兮', 'age': 20}
# 修改原来的数据,查看现在的数据是否改变
dic1["age"] = 33
print(dic1) # {'name': '兮兮', 'age': 33}
print(dic2) # {'name': '兮兮', 'age': 20}