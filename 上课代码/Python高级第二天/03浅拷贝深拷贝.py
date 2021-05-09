"""
copy模块:
    copy()      浅拷贝-->针对复杂类型数据中只有简单类型数据
    deepcopy()  深拷贝-->针对复杂类型数据中还有简单类型数据
"""
import copy
ls = [1,2,3]
ls1 = copy.copy(ls) # 浅拷贝

# 修改原来的ls
ls.append(4)
print(ls)
print(ls1)

ls2 = [1,[2,[3,4,[1,2]]]]
ls3 = copy.deepcopy(ls2) # 深拷贝
print(ls3)
# 修改ls2
ls2[1][1] = 99
print(ls2)
print(ls3)