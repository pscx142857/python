CREATE TABLE `teacher` (
  `t_id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '学生id',
  `t_name` varchar(20) DEFAULT NULL COMMENT '学生姓名',
  PRIMARY KEY (`t_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COMMENT='学生表';

CREATE TABLE `teacher_class` (
  `t_id` int(10) unsigned NOT NULL COMMENT '学生id',
  `class_id` int(10) unsigned NOT NULL COMMENT '学生id'
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COMMENT='学生表';

insert into teacher (t_id, t_name)
values (1,'刘老师'),(2,'唐老师'),(3,'段老师');

insert into teacher_class (t_id, class_id)
values (1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,2),(3,3);

# 多对多,查询刘老师给哪些班级上过课
select t_name,class_name
from teacher join teacher_class tc on teacher.t_id = tc.t_id
             join class c on tc.class_id = c.class_id
where teacher.t_id=1;