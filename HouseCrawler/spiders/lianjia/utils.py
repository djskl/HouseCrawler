# coding:utf-8
from scrapy.conf import settings
from scrapy.exporters import CsvItemExporter

HOUSE_PRICE_CONDS = ["p1p2p3", "p4", "p5", "p6", "p7", "p8"]
HOUSE_ROOM_CONDS = ["l1", "l2", "l3", "l4", "l5"]

BASE_URLS = [
    "https://bj.lianjia.com/ershoufang/dongcheng/ng1hu1nb1/",
    "https://bj.lianjia.com/ershoufang/xicheng/ng1hu1nb1/",
    "https://bj.lianjia.com/ershoufang/chaoyang/ng1hu1nb1/",
    "https://bj.lianjia.com/ershoufang/haidian/ng1hu1nb1/",
    "https://bj.lianjia.com/ershoufang/fengtai/ng1hu1nb1/",
    "https://bj.lianjia.com/ershoufang/shijingshan/ng1hu1nb1/",
    "https://bj.lianjia.com/ershoufang/tongzhou/ng1hu1nb1/",
    "https://bj.lianjia.com/ershoufang/changping/ng1hu1nb1/",
    "https://bj.lianjia.com/ershoufang/daxing/ng1hu1nb1/",
    "https://bj.lianjia.com/ershoufang/yizhuangkaifaqu/ng1hu1nb1/",
    "https://bj.lianjia.com/ershoufang/shunyi/ng1hu1nb1/",
    "https://bj.lianjia.com/ershoufang/fangshan/ng1hu1nb1/",
    "https://bj.lianjia.com/ershoufang/mentougou/ng1hu1nb1/",
    "https://bj.lianjia.com/ershoufang/pinggu/ng1hu1nb1/",
    "https://bj.lianjia.com/ershoufang/huairou/ng1hu1nb1/",
    "https://bj.lianjia.com/ershoufang/miyun/ng1hu1nb1/",
    "https://bj.lianjia.com/ershoufang/yanqing/ng1hu1nb1/"
]


def getTotals(response):
    xpath_cond = "//h2[contains(concat(' ', normalize-space(@class), ' '), ' total fl ')]/span/text()"
    rst = response.xpath(xpath_cond).extract_first()
    if rst:
        return int(rst.strip())
    return 0


def getHouseInfo(response):
    return {
        "链家编号": response.xpath(
            '//div[@class="aroundInfo"]/div[@class="houseRecord"]/span[@class="info"]/text()').extract_first(),
        "价格": response.xpath(
            "//div[contains(concat(' ', normalize-space(@class), ' '), ' price ')]/span[contains(concat(' ', normalize-space(@class), ' '), ' total ')]/text()").extract_first(),
        "关注": response.xpath("//span[@id='favCount']/text()").extract_first(),
        "看过": response.xpath("//span[@id='cartCount']/text()").extract_first(),
        "区县": response.xpath(u"//span[text()='所在区域']/parent::div/span[2]/a[1]/text()").extract_first(),
        "商圈": response.xpath(u"//span[text()='所在区域']/parent::div/span[2]/a[2]/text()").extract_first(),
        "环线": response.xpath(u"//span[text()='所在区域']/parent::div/span[2]/text()[2]").extract_first(),
        "小区": response.xpath('//div[@class="aroundInfo"]/div[@class="communityName"]/a/text()').extract_first(),
        "房屋户型": response.xpath(u"//span[text()='房屋户型']/parent::li/text()").extract_first(),
        "所在楼层": response.xpath(u"//span[text()='所在楼层']/parent::li/text()").extract_first(),
        "建筑面积": response.xpath(u"//span[text()='建筑面积']/parent::li/text()").extract_first(),
        "户型结构": response.xpath(u"//span[text()='户型结构']/parent::li/text()").extract_first(),
        "套内面积": response.xpath(u"//span[text()='套内面积']/parent::li/text()").extract_first(),
        "建筑类型": response.xpath(u"//span[text()='建筑类型']/parent::li/text()").extract_first(),
        "房屋朝向": response.xpath(u"//span[text()='房屋朝向']/parent::li/text()").extract_first(),
        "建筑结构": response.xpath(u"//span[text()='建筑结构']/parent::li/text()").extract_first(),
        "装修情况": response.xpath(u"//span[text()='装修情况']/parent::li/text()").extract_first(),
        "梯户比例": response.xpath(u"//span[text()='梯户比例']/parent::li/text()").extract_first(),
        "供暖方式": response.xpath(u"//span[text()='供暖方式']/parent::li/text()").extract_first(),
        "配备电梯": response.xpath(u"//span[text()='配备电梯']/parent::li/text()").extract_first(),
        "产权年限": response.xpath(u"//span[text()='产权年限']/parent::li/text()").extract_first(),
        "挂牌时间": response.xpath(u"//span[text()='挂牌时间']/parent::li/text()").extract_first(),
        "上次交易": response.xpath(u"//span[text()='上次交易']/parent::li/text()").extract_first(),
        "交易权属": response.xpath(u"//span[text()='交易权属']/parent::li/text()").extract_first(),
        "房屋用途": response.xpath(u"//span[text()='房屋用途']/parent::li/text()").extract_first(),
        "房屋年限": response.xpath(u"//span[text()='房屋年限']/parent::li/text()").extract_first(),
        "产权所属": response.xpath(u"//span[text()='产权所属']/parent::li/text()").extract_first(),
        "抵押信息": response.xpath(u"//span[text()='抵押信息']/parent::li/span[2]/text()").extract_first(),
        "房本备件": response.xpath(u"//span[text()='房本备件']/parent::li/text()").extract_first(),
        "链接": response.url
    }


FIELDS_TO_EXPORT = [
    "链家编号",
    "价格",
    "房屋户型",
    "建筑面积",
    "上次交易",
    "挂牌时间",
    "看过",
    "区县",
    "商圈",
    "环线",
    "小区",
    "关注",
    "所在楼层",
    "户型结构",
    "套内面积",
    "建筑类型",
    "房屋朝向",
    "建筑结构",
    "装修情况",
    "梯户比例",
    "供暖方式",
    "配备电梯",
    "产权年限",
    "交易权属",
    "房屋用途",
    "房屋年限",
    "产权所属",
    "房本备件",
    "抵押信息",
    "链接"
]


class HouseCsvExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        delimiter = settings.get('CSV_DELIMITER', ',')
        kwargs['delimiter'] = delimiter
        kwargs['fields_to_export'] = FIELDS_TO_EXPORT
        super(HouseCsvExporter, self).__init__(*args, **kwargs)