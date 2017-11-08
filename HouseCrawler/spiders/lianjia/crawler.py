# coding:utf-8
import json
import scrapy
from HouseCrawler.spiders.lianjia.utils import getTotals, HOUSE_ROOM_CONDS, HOUSE_PRICE_CONDS, BASE_URLS, getHouseInfo


class LianjiaSpider(scrapy.Spider):
    name = "lianjia_for_sale"

    start_urls = BASE_URLS

    def parse_house_item(self, response):
        yield getHouseInfo(response)

    def parse_house_list(self, response):
        for item_url in response.xpath("//ul[@class='sellListContent']/li/a/@href"):
            next_url = item_url.extract()
            yield response.follow(next_url, self.parse_house_item)

    def parse_house_pages(self, response):
        page_data = json.loads(response.xpath("//div[@class='page-box house-lst-page-box']/@page-data").extract_first())
        total_pages = page_data["totalPage"]
        for idx in range(total_pages):
            base_url = response.url[:-1] if response.url.endswith("/") else response.url
            next_url = base_url + "pg%d" % (idx + 1)
            yield response.follow(next_url, self.parse_house_list)

    def parse_house_price(self, response):
        totals = getTotals(response)

        if totals < 1:
            return

        if totals < 3001:
            yield response.follow(response.url, self.parse_house_pages, dont_filter=True)

        if totals > 3000:
            base_url = response.url
            if base_url.endswith("/"):
                base_url = base_url[:-1]

            for room_cond in HOUSE_ROOM_CONDS:
                next_url = base_url + room_cond
                yield response.follow(next_url, self.parse_house_pages)

    def parse(self, response):

        totals = getTotals(response)

        if totals < 1:
            return

        if totals < 3001:
            yield response.follow(response.url, self.parse_house_pages, dont_filter=True)

        if totals > 3000:
            base_url = response.url
            if base_url.endswith("/"):
                base_url = base_url[:-1]

            for price_cond in HOUSE_PRICE_CONDS:
                next_url = base_url + price_cond
                yield response.follow(next_url, self.parse_house_price)
