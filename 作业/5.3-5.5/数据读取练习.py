class Student(object):
    def __init__(self,name,subjects):
        self.name = name
        self.subjects = subjects
    def __str__(self):
        return f"{self.name}\t\t{self.subjects}"

students = list()
# 打开文件
fp = open("data.txt","r",encoding="utf8")
# 操作文件
data = fp.read()
ls = data.strip("\n").split("\n")
for i in ls:
    ls1 = i.split(",")
    ls2 = ls1[1::]
    stu = Student(ls2[0],ls2)
    print(stu)
    students.append(stu)
# 关闭文件
fp.close()
