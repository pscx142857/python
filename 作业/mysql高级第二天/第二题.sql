/*
 2.新建数据表使用sql 语句
公司新闻表（ID，新闻标题，作者，新闻内容，发布时间，点击次数）

     create table `表名`(
        `字段名1` 字段类型,
        `字段名2` 字段类型,
        ...)[选项]
 */
 create table `news`(
     `id` int primary key,
     `title` varchar(50),
     `author` varchar(50),
     `content` text,
     `date` timestamp,
     `times` int
 )charset=`utf8`