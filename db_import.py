import psycopg2

def check(house):
    if len(house) < 30: return False
    tmp = [True] + house[:15]
    t = reduce(lambda x, y: x and len(y)>0, tmp)
    return t

def insert_houses(cur, csv_file):
    with open(csv_file) as houses:
        houses.readline()
        idx = 1
        for line in houses:
            house = line.split(",")
            if not check(house): continue
            hid = house[0]
            cur.execute("select id from zs where id=%s", [hid])
            dao = cur.fetchone()
            try:
                if dao:
                    cur.execute(
                        "update zs set price=%s,huxing=%s,area=%s,lasttrade=%s,ctime=%s,visits=%s,quxian=%s,shangquan=%s,"
                        "huanxian=%s,xiaoqu=%s,guanzhu=%s,louceng=%s,jiegou=%s,taonei=%s,leixing=%s,chaoxiang=%s,"
                        "jianzhujiegou=%s,zhuangxiu=%s,tihubili=%s,gongnuan=%s,dianti=%s,chanquannianxian=%s,quanshu=%s,"
                        "yongtu=%s,fangwunianxian=%s,chanquansuoshu=%s,fanbenbeijian=%s,diya=%s,link=%s WHERE id=%s",
                        house[1:] + [hid])
                else:
                    cur.execute(
                        "insert into zs VALUES(%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,"
                        "%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s)", house)

            except Exception, e:
                print idx, "ERROR", e, line
                idx = idx + 1


with psycopg2.connect(host="10.0.83.147", database="lianjia", user="postgres") as conn:
    with conn.cursor() as cur:
        insert_houses(cur, "/mnt/f25/Downloads/20180317_zs_lj.csv")

conn.commit()
conn.close()
