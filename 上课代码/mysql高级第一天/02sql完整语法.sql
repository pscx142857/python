# select 选项 [字段表达式]  [from 子句]  [where表达式 子句]  [group by 子句]  [having 子句]  [order by 子句]  [limit 子句]

# 去重,默认是显示全部,distinct去重
select distinct class_id
from student;
# 查询学生表中所有的信息
select *
from student;
# 查询学生表中所有的学号和姓名,别名可以用as 也可以不写
select stu_no as number, stu_name name
from student;
# 统计有多少个学生,聚合函数除了count 还有max min avg sum
select count(*) 总数
from student;
# from,查询学生为曹操的所在的班级是哪个班
select stu_name,class_name
from student join class c on student.class_id = c.class_id
where stu_name = '曹操'
# where对数据源进行过滤
/*
    1.比较运算符:< > = <= >= !=(<>)
    2.like: %(任意长度任意字符)   _(一个长度任意字符)
    3.in 或者 not in :在不在集合里面
 */
# 查询学生id不等2的学生信息
select *
from student where stu_id <> 2;
select *
from student where stu_id != 2;
# 查询姓袁的学生的信息
select *
from student where stu_name like "袁%";
# 查询姓袁 名字有3个字的学生的信息
select *
from student where stu_name like "袁__";
# 查询学生id为1,4,5的学生信息
select *
from student where stu_id in(1,4,5);
# 查询stu_name 不是 曹操 袁绍 袁术 的学生信息
select *
from student where stu_name not in("操作","袁绍","袁术");
# 查询id是1-3之间的学生,包含1和3
select *
from student where stu_id between 1 and 3;
# 查询id不是1-3之间的学生
select *
from student where stu_id not between 1 and 3;
# 查询没有班级的学生
select *
from student
where class_id is null;
# 查询有班级的学生
select *
from student
where class_id is not null;
# 查询每个班的学生人数
select class_id,count(class_id)
from student
group by class_id;
# 插入money字段
alter table student add money decimal(10,2)
# 修改money的值
update student set money = 100000
# 查询每个班级的零花钱的平均值
select class_id,avg(money)
from student
group by class_id;
# 查询班级零花钱平均值大于30000的班级
select class_id,avg(money)
from student
group by class_id
having avg(money) > 30000;
# 查询每个班的学生姓名,group_concat(字段名):将分组之后的字段中的内存,组合成一个字符串
select group_concat(stu_name),class_id
from student
group by class_id;
# 按零花钱排序,desc 降序,默认升序
select *
from student
order by money desc;
# 对多个字段排序
select *
from student
order by class_id,money desc;
# 查询最有钱的3个同学,limit 起始索引(默认是0),显示条数
select *
from student
order by money desc
limit 3;