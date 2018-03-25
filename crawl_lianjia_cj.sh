#!/usr/bin/env bash
ndir=$(cd `dirname $0`; pwd)
cd $ndir

FILENAME=$(date +%Y%m%d)_cj_lj
OUTPUT_DIR=$ndir/data/lianjia/cj

/usr/bin/python2 /usr/bin/scrapy crawl lianjia_cj -t lianjia_cj_csv -o ${OUTPUT_DIR}/${FILENAME}.csv -L INFO >& ${OUTPUT_DIR}/${FILENAME}.logs

timeout 300 \cp ${OUTPUT_DIR}/${FILENAME}.csv /mnt/jianguo/lianjian/

