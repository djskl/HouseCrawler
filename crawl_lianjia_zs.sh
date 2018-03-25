#!/usr/bin/env bash
ndir=$(cd `dirname $0`; pwd)
cd $ndir

FILENAME=$(date +%Y%m%d)_zs_lj
OUTPUT_DIR=$ndir/data/lianjia/zs

/usr/bin/python2 /usr/bin/scrapy crawl lianjia_for_sale -t lianjia_csv -o ${OUTPUT_DIR}/${FILENAME}.csv -L INFO >& ${OUTPUT_DIR}/${FILENAME}.logs

timeout 300 \cp ${OUTPUT_DIR}/${FILENAME}.csv /mnt/jianguo/lianjian/

