nohup scrapy crawl fang_chengjiao -t fangtx_csv -o $(date +%Y%m%d)_cj_fx.csv -L INFO >& $(date +%Y%m%d)_cj_fx.logs & 
