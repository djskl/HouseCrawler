# coding:utf-8
import re
import scrapy

from HouseCrawler.spiders.fangtx_cj.utils import BASE_URLS, getTotals, COND_AR, COND_RM, COND_PR


class FangSpider(scrapy.Spider):

    name = "fang_chengjiao"

    start_urls = BASE_URLS

    def parse_house_item(self, response):
        info_top = response.xpath("//div[@id='chengjiaoxq_B02_02']//ul/li")
        tmp = info_top.xpath("//b/text()").extract()
        price = tmp[0]
        danjia = tmp[1]
        chaoxiang = tmp[2]

        mianji = response.xpath(u"//b[text()='面积：']/parent::p/text()").extract_first()
        louceng = response.xpath(u"//b[text()='楼层：']/parent::p/text()").extract_first()

        pos_info = response.xpath(u"//b[text()='小区：']/parent::p/a/text()").extract()
        xiaoqu = pos_info[0]
        quxian = pos_info[1]
        shangquan = pos_info[2]

        cj_date = response.xpath("//div[@class='title title1']//span/text()").extract_first()
        tmp_cj_date = re.split(r"\s+", cj_date.strip())
        cj_date = tmp_cj_date[0]

        huxing = response.xpath("//div[@class='title title1']/h1/text()").extract_first()
        tmp = re.split(r"\s+", huxing.strip())
        huxing = tmp[1]

        yield {
            "日期": cj_date,
            "价格": price,
            "单价": danjia,
            "户型": huxing,
            "面积": mianji,
            "朝向": chaoxiang,
            "楼层": louceng,
            "小区": xiaoqu,
            "商圈": shangquan,
            "区县": quxian,
            "链接": response.url
        }


    def parse_houses(self, response):
        for dl in response.xpath("//div[@class='houseList']/dl/dd"):
            next_url = dl.xpath('p[@class="title"]/a/@href').extract_first()
            yield response.follow(next_url, self.parse_house_item)

    def parse_house_by_areas(self, response):
        totals, pages = getTotals(response)
        if totals < 1: return

        base_url = response.url
        if base_url.endswith("/"): base_url = base_url[:-1]

        for idx in range(pages):
            next_url = base_url + "-i3%d"%(idx+1)
            yield response.follow(next_url, self.parse_houses)


    def parse_house_by_rooms(self, response):
        totals, pages = getTotals(response)
        if totals < 1: return

        base_url = response.url
        if base_url.endswith("/"): base_url = base_url[:-1]

        if totals < 3001:
            for idx in range(pages):
                next_url = base_url + "-i3%d"%(idx+1)
                yield response.follow(next_url, self.parse_houses)

        if totals > 3000:
            for area_cond in COND_AR:
                next_url = base_url + "-" + area_cond
                yield response.follow(next_url, self.parse_house_by_areas)


    def parse_house_by_price(self, response):
        totals, pages = getTotals(response)
        if totals < 1: return

        base_url = response.url
        if base_url.endswith("/"): base_url = base_url[:-1]

        if totals < 3001:
            for idx in range(pages):
                next_url = base_url + "-i3%d"%(idx+1)
                yield response.follow(next_url, self.parse_houses)

        if totals > 3000:
            for room_cond in COND_RM:
                next_url = base_url + "-" + room_cond
                yield response.follow(next_url, self.parse_house_by_rooms)


    def parse(self, response):

        totals, pages = getTotals(response)

        if totals < 1:
            return

        base_url = response.url
        if base_url.endswith("/"): base_url = base_url[:-1]

        if totals < 3001:
            for idx in range(pages):
                next_url = base_url + "-i3%d"%(idx+1)
                yield response.follow(next_url, self.parse_houses)

        if totals > 3000:
            for price_cond in COND_PR:
                next_url = base_url + "-" + price_cond
                yield response.follow(next_url, self.parse_house_by_price)
