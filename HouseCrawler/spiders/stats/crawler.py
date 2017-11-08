# coding:utf-8
import scrapy

ROOT_URL = "http://www.anjuke.com/fangjia/beijing"

AREAS = ["chaoyang", "haidian", "dongchenga", "xicheng", "fengtai", "tongzhou", "shijingshan", "changping", "daxing",
         "shunyi", "fangshan", "mentougou", "miyun", "huairou", "pinggua", "yanqing"
         ]

BASE_URLS = []
for idx in range(10):
    BASE_URLS = BASE_URLS + [ROOT_URL+str(2008+idx)+"/"+ ar for ar in AREAS]

class HistoryPriceSpider(scrapy.Spider):

    name = "history_price"

    start_urls = BASE_URLS

    def parse(self, response):
        x = response.xpath("//h2/text()").extract_first()
        years = x[:4]
        pos = x[5:-2]

        for fj in response.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' fjlist-box ')][1]/ul/li"):
            d = fj.xpath("a/b/text()").extract_first()[5:-2]
            p = fj.xpath("a/span/text()").extract_first()[:-3]
            yield {
                "区县": pos,
                "年份": years,
                "月份": d,
                "价格": p
            }