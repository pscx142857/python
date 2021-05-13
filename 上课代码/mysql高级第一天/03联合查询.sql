# union连表查询,默认会去重,加上all就不会了
select *
from student
union all
select *
from student;

(select *
from student
order by stu_id limit 100)
union all
(select *
from student
order by stu_id desc limit 100);