# coding:utf-8
import json
import scrapy

from HouseCrawler.spiders.lianjia_cj.utils import BASE_URLS, getHouseInfo

HOUSE_PRICE_CONDS = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"]
HOUSE_ROOM_CONDS = ["l1", "l2", "l3", "l4l5"]


class LianjiaSpider(scrapy.Spider):

    name = "lianjia_cj"

    start_urls = BASE_URLS

    def getTotals(self, response):
        totals = response.xpath('//div[@class="total fl"]/span/text()').extract_first().strip()
        pages = response.xpath('//div[@class="page-box house-lst-page-box"]/@page-data').extract_first()
        page = json.loads(pages)
        return int(totals), page["totalPage"]

    def parse_house_item(self, response):
        ljid = response.xpath(u"//span[text()='链家编号']/parent::li/text()").extract_first()
        ljid = ljid.strip()
        if ljid:
            yield getHouseInfo(response)

    def parse_houses(self, response):
        all_urls = response.xpath("//ul[@class='listContent']/li/a/@href").extract()
        for next_url in all_urls:
            yield response.follow(next_url, self.parse_house_item)


    def parse_house_by_room(self, response):
        totals, pages = self.getTotals(response)

        if totals < 1:
            return

        base_url = response.url
        if base_url.endswith("/"): base_url = base_url[:-1]

        for idx in range(pages):
            next_url = base_url + "pg%d" % (idx + 1)
            yield response.follow(next_url, self.parse_houses)


    def parse_house_by_price(self, response):
        totals, pages = self.getTotals(response)

        if totals < 1:
            return

        base_url = response.url
        if base_url.endswith("/"): base_url = base_url[:-1]

        if totals < 3001:
            for idx in range(pages):
                next_url = base_url + "pg%d" % (idx + 1)
                yield response.follow(next_url, self.parse_houses)

        if totals > 3000:
            for romm_cond in HOUSE_ROOM_CONDS:
                next_url = base_url + romm_cond
                yield response.follow(next_url, self.parse_house_by_room)


    def parse(self, response):
        totals, pages = self.getTotals(response)

        if totals < 1:
            return

        base_url = response.url
        if base_url.endswith("/"): base_url = base_url[:-1]

        if totals < 3001:
            for idx in range(pages):
                next_url = base_url + "pg%d" % (idx + 1)
                yield response.follow(next_url, self.parse_houses)

        if totals > 3000:
            for price_cond in HOUSE_PRICE_CONDS:
                next_url = base_url + price_cond
                yield response.follow(next_url, self.parse_house_by_price)
