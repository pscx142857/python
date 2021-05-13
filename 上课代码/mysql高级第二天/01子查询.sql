/*
子查询:
    一个sql查询语句出现在另一个sql查询语句内,就是子查询语句
        select查询语句 嵌套另外select查询语句
        原本需要使用多条sql查询语句才能查询出的结果,使用子查询只需要一个语句
    将一条sql查询语句的结果作为另一条sql查询语句使用
*/
# 查询学生的零花钱大于平均零花钱的学生信息
select avg(money)
from student; # 26885.714286

select *
from student
where money > 26885.714286;

# 合并,就是子查询
select *
from student
where money > (select avg(money)
from student);
/*
 子查询分类:
    按子查询位置分:
        where型子查询
        from型子查询
    按子查询的结果进行划分:
        列子查询,子查询结果为一列
        表子查询,子查询的结果为表

 */
 # 查询最有钱的3位学生,按照零花钱进行升序排列
select *
from (select *
from student
order by money desc limit 3) as m
order by money;
# 查询零花钱大于8000的学生班级信息
select *
from class
where class_id in (select distinct class_id
from student
where money>8000);
# 查询哪些班级没有学生
select distinct class_id
from student;

select *
from class
where class_id not in (1,11);
# 合并后的子查询
select *
from class
where class_id not in (select distinct class_id
from student);
# 查询每个班级最有钱的学生信息
select class_id,max(money)
from student
group by class_id;

select *
from student
where (class_id,money) in (select class_id,max(money)
from student
group by class_id);