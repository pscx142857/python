/*
    外键约束:
        主表和从表,主表约束从表
            从表里面的约束字段,不能随意修改和增加
            主表里面的约束字段,不能随意修改和删除
    缺点:
        会严重影响我们mysql数据库的性能
 */
 # 添加外键
alter table student add foreign key(class_id) references class (class_id);
# 查询建表语句
show create table `student`;
# 删除外键
alter table student drop foreign key student_ibfk_1;

# 高级部分
alter table student add constraint `fk_stu_class` foreign key (class_id)
references class (class_id) on delete set null on update cascade;

alter table student drop foreign key `fk_stu_class`;
alter table student drop key `fk_stu_class`;