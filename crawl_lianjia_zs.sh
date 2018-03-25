#!/usr/bin/env bash
ndir=$(cd `dirname $0`; pwd)
cd $ndir

filepath=$ndir/data/lianjia/zs/$(date +%Y%m%d)_zs_lj.csv

/usr/bin/python2 /usr/bin/scrapy crawl lianjia_for_sale -t lianjia_csv -o $filepath -L INFO >& $ndir/$(date +%Y%m%d)_zs_lj.logs

timeout 300 \cp $filepath /mnt/jianguo/lianjian/

