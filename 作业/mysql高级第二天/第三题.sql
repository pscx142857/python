/*
 3.编写sql语句实现向新闻表中插入数据
 （ID，新闻标题，作者，新闻内容，发布时间，点击次数）
 */
 insert into `news` (title,author,content,times)
    values(1,'重大新闻','中原一点红','我就是内容',25000);

 insert into `news` (id,title,author,content,times)
    values(2,'重大新闻2','中点红','我就最大的人',5000);