#校验长度
/usr/bin/python2.7 /root/PycharmProjects/HouseCrawler/db_import.py
1 ERROR invalid input syntax for integer: ""
LINE 1: insert into zs VALUES('' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,''...
                                                      ^
 ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,https://bj.lianjia.com/ershoufang/

Traceback (most recent call last):
  File "/root/PycharmProjects/HouseCrawler/db_import.py", line 31, in <module>
    insert_houses(cur, "/root/Downloads/20180317_zs_lj.csv")
  File "/root/PycharmProjects/HouseCrawler/db_import.py", line 10, in insert_houses
    cur.execute("select id from zs where id=%s", [hid])
psycopg2.InternalError: current transaction is aborted, commands ignored until end of transaction block



import psycopg2

def insert_houses(cur, csv_file):
    with open(csv_file) as houses:
        houses.readline()
        idx = 1
        for line in houses:
            house = line.split(",")
            hid = house[0]
            cur.execute("select id from zs where id=%s", [hid])
            dao = cur.fetchone()

            try:
                if dao:
                    cur.execute("update zs set price=%s,huxing=%s,area=%s,lasttrade=%s,ctime=%s,visits=%s,quxian=%s,shangquan=%s,"
                                "huanxian=%s,xiaoqu=%s,guanzhu=%s,louceng=%s,jiegou=%s,taonei=%s,leixing=%s,chaoxiang=%s,"
                                "jianzhujiegou=%s,zhuangxiu=%s,tihubili=%s,gongnuan=%s,dianti=%s,chanquannianxian=%s,quanshu=%s,"
                                "yongtu=%s,fangwunianxian=%s,chanquansuoshu=%s,fanbenbeijian=%s,diya=%s,link=%s WHERE id=%s",house[1:]+[hid])
                else:
                    cur.execute("insert into zs VALUES(%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,"
                                "%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s)", house)

            except Exception, e:
                print idx, "ERROR", e, line
                idx = idx + 1



with psycopg2.connect(host="10.0.83.147", database="lianjia", user="postgres") as conn:
    with conn.cursor() as cur:
        insert_houses(cur, "/root/Downloads/20180317_zs_lj.csv")

conn.commit()
conn.close()