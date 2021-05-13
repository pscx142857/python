/*
    索引:为了极大的提高sql语句的查询速度
        针对的是具体的某个字段
    创建索引:是由mysql帮助自动创建

    索引分类:
        主索引: 创建主键的时候,同时这个主键的字段创建成主索引
        唯一索引: 创建唯一键的时候,同时将这个键创建成唯一索引
        普通索引:key
 */
explain select *
from student
where stu_name = '曹操';

explain select *
from student
where stu_id=4;