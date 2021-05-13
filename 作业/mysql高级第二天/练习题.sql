DROP TABLE IF EXISTS `student_copy`;
CREATE TABLE `student_copy` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` char(20) NOT NULL,
  `sex` char(20) DEFAULT NULL,
  `birth` year(4) DEFAULT NULL,
  `department` char(10) DEFAULT NULL,
  `address` char(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `score`;
CREATE TABLE `score` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `stu_id` int(10) NOT NULL,
  `c_name` char(20) DEFAULT NULL,
  `grade` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `score_ibfk_1` (`stu_id`),
  CONSTRAINT `score_ibfk_1` FOREIGN KEY (`stu_id`) REFERENCES `student_copy` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;


insert  into `student_copy`(`id`,`name`,`sex`,`birth`,`department`,`address`) values (1,'张老大','男',1985,'计算机系','北京市海淀区');
insert  into `student_copy`(`id`,`name`,`sex`,`birth`,`department`,`address`) values (2,'张老二','男',1986,'中文系','北京市昌平区');
insert  into `student_copy`(`id`,`name`,`sex`,`birth`,`department`,`address`) values (3,'张三','女',1990,'中文系','湖南省永州市');
insert  into `student_copy`(`id`,`name`,`sex`,`birth`,`department`,`address`) values (4,'李四','男',1990,'英语系','辽宁省阜新市');
insert  into `student_copy`(`id`,`name`,`sex`,`birth`,`department`,`address`) values (5,'王五','女',1991,'英语系','福建省厦门市');
insert  into `student_copy`(`id`,`name`,`sex`,`birth`,`department`,`address`) values (6,'王六','男',1988,'计算机系','湖南省衡阳市');


insert  into `score`(`id`,`stu_id`,`c_name`,`grade`) values (1,1,'计算机',98);
insert  into `score`(`id`,`stu_id`,`c_name`,`grade`) values (2,1,'英语',80);
insert  into `score`(`id`,`stu_id`,`c_name`,`grade`) values (3,2,'计算机',65);
insert  into `score`(`id`,`stu_id`,`c_name`,`grade`) values (4,2,'中文',88);
insert  into `score`(`id`,`stu_id`,`c_name`,`grade`) values (5,3,'中文',95);
insert  into `score`(`id`,`stu_id`,`c_name`,`grade`) values (6,3,'计算机',70);
insert  into `score`(`id`,`stu_id`,`c_name`,`grade`) values (7,4,'计算机',70);
insert  into `score`(`id`,`stu_id`,`c_name`,`grade`) values (8,4,'英语',92);
insert  into `score`(`id`,`stu_id`,`c_name`,`grade`) values (9,5,'英语',94);
insert  into `score`(`id`,`stu_id`,`c_name`,`grade`) values (10,5,'计算机',90);
insert  into `score`(`id`,`stu_id`,`c_name`,`grade`) values (11,6,'计算机',90);
insert  into `score`(`id`,`stu_id`,`c_name`,`grade`) values (12,6,'英语',85);


# 1. 查询"张老大"成绩大于90分的成绩信息
select *
from score join student_copy sc on sc.id = score.stu_id
where name = '张老大' and grade>90;
# 2. 查询"计算机"的平均成绩
select avg(grade)
from score
where c_name='计算机';
# 3. 查询stu_id 为 "3" 的学生姓名以及参加的考试信息
select *
from score join student_copy sc on sc.id = score.stu_id
where stu_id=3;
# 4. 查询参与"计算机"考试的学生有多少位
select count(*)
from score
where c_name='计算机';
# 5. 查询参与"计算机"考试的学生姓名
select name
from student_copy join score s on student_copy.id = s.stu_id
where c_name='计算机';
# 1.查询student_copy表的所有记录
select *
from student_copy;
# 2.查询student_copy表的第2条到4条记录
select *
from student_copy
limit 1,3;
# 3.从student_copy表查询所有学生的学号（id）、姓名（name）和院系（department）的信息
select id,name,department
from student_copy;
# 4.从student_copy表中查询计算机系和英语系的学生的信息
select *
from student_copy
where department in ('计算机系','英语系');
# 5.从student_copy表中查询年龄在18~35岁的学生信息     1986-2003
select *
from student_copy
where birth between 1986 and 2003;
# 1.查询每个院系有多少人
select department,count(*)
from student_copy
group by department;
# 2.查询每个科目的最高分
select c_name,max(grade)
from score
group by c_name;
# 3.查询李四的考试科目（c_name）和考试成绩（grade）
select c_name,grade
from score join student_copy sc on sc.id = score.stu_id
where name='李四';
# 4.所有学生的信息和考试信息
select *
from student_copy join score s on student_copy.id = s.stu_id;
# 5.计算每个学生的总成绩
select name,sum(grade)
from score join student_copy sc on sc.id = score.stu_id
group by stu_id;
# 1.计算每个考试科目的平均成绩
select c_name,avg(grade)
from score
group by c_name;
# 2.计算每个学生的平均成绩？？？
select name,avg(grade)
from score join student_copy sc on sc.id = score.stu_id
group by stu_id;
# 3.查询计算机成绩低于95的学生信息
select *
from student_copy join score s on student_copy.id = s.stu_id
where grade < 95 and c_name='计算机';
# 4.查询每个学科的平均成绩
select c_name,avg(grade)
from score
group by c_name;
# 5.将计算机考试成绩降序排列
select *
from score
where c_name='计算机'
order by grade desc;
# 1.查询姓张或者姓王的同学的姓名、院系和考试科目及成绩
select name,department,c_name,grade
from student_copy join score s on student_copy.id = s.stu_id
where name like '张%' or name like '王%';
# 2.查询都是湖南的学生的姓名、年龄、院系和考试科目及成绩
select name,birth,department,c_name,grade
from student_copy join score s on student_copy.id = s.stu_id
where address like '湖南%';
# 3.查询出每门课程都大于80分的学生姓名
# 类似于这个题目：查询所有成绩都及格的学生
select *
from student_copy
where id in (select stu_id
from score
group by stu_id
having min(grade) > 80);

select stu_id
from score
group by stu_id
having min(grade) > 80;
# 4.查询同时参加计算机和英语考试的学生的信息
select a.*
from student_copy a,score b,score c
where a.id=b.stu_id
and a.id=c.stu_id
and b.c_name='计算机'
and c.c_name='英语';

select * from student_copy where id in (
select stu_id from score where c_name ='计算机' and stu_id in(
select stu_id from score where c_name ='英语'));
# 查询湖南省的人,并且同时参加中文 和 计算机 考试的学生信息
select *
from student_copy
where address like '湖南%' and id in (select id from student_copy where id in (
select stu_id from score where c_name ='计算机' and stu_id in(
select stu_id from score where c_name ='中文')));
# 查询比中文系平均成绩高的 其余系学生信息
select avg(grade)
from score join student_copy sc on sc.id = score.stu_id
where department='中文系';

select *
from student_copy join score s on student_copy.id = s.stu_id
where department != '中文系' and grade >(select avg(grade)
from score join student_copy sc on sc.id = score.stu_id
where department='中文系');

# (拓展提升) 查询男生的比例
select concat(
  round(
    (
      (select count(*) from student_copy where sex='男')
                       /
                     (select count(*) from student_copy)
      ) * 100,2
    ) , '%'
  );
# (拓展提升) 查询姓张的同学 占 总学生数量的比例
select concat(
  round(
    (
      (select count(*) from student_copy where name like '张%')
                       /
                     (select count(*) from student_copy)
      ) * 100,2
    ) , '%'
  );