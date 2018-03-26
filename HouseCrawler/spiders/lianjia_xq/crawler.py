# coding:utf-8
import scrapy

class LianjiaSpider(scrapy.Spider):

    name = "lianjia_xq"

    start_urls = ["https://bj.lianjia.com/xiaoqu/tongzhou/"]

    def parse_titles(self, response):
        all_titles = response.xpath("//li[contains(@class, 'xiaoquListItem')]//div[@class='title']/a/text()").extract()
        for title in all_titles:
            yield {"title":title}

    def parse(self, response):
        base_url = response.url
        if base_url.endswith("/"): base_url = base_url[:-1]

        for idx in range(22):
            next_url = base_url + "pg%d" % (idx + 1)
            yield response.follow(next_url, self.parse_titles)
