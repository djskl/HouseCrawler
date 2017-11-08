ndir=$(cd `dirname $0`; pwd)
cd $ndir
/usr/bin/python2 /usr/bin/scrapy crawl lianjia_for_sale -t lianjia_csv -o $ndir/$(date +%Y%m%d)_zs_lj.csv -L INFO >& $ndir/$(date +%Y%m%d)_zs_lj.logs
