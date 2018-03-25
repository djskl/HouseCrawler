# coding:utf-8
from scrapy.conf import settings
from scrapy.exporters import CsvItemExporter

HOUSE_PRICE_CONDS = ["bp0ep300", "bp301ep400", "bp401ep500", "bp501ep600", "bp601ep2000"]
HOUSE_ROOM_CONDS = ["l1", "l2", "l3", "l4", "l5"]

BASE_URLS = [
    "https://bj.lianjia.com/ershoufang/dongcheng/ng1hu1nb1/",
    # "https://bj.lianjia.com/ershoufang/xicheng/ng1hu1nb1/",
    # "https://bj.lianjia.com/ershoufang/chaoyang/ng1hu1nb1/",
    # "https://bj.lianjia.com/ershoufang/haidian/ng1hu1nb1/",
    # "https://bj.lianjia.com/ershoufang/fengtai/ng1hu1nb1/",
    # "https://bj.lianjia.com/ershoufang/shijingshan/ng1hu1nb1/",
    # "https://bj.lianjia.com/ershoufang/tongzhou/ng1hu1nb1/",
    # "https://bj.lianjia.com/ershoufang/changping/ng1hu1nb1/",
    # "https://bj.lianjia.com/ershoufang/daxing/ng1hu1nb1/",
    # "https://bj.lianjia.com/ershoufang/yizhuangkaifaqu/ng1hu1nb1/",
    # "https://bj.lianjia.com/ershoufang/shunyi/ng1hu1nb1/",
    # "https://bj.lianjia.com/ershoufang/fangshan/ng1hu1nb1/",
    # "https://bj.lianjia.com/ershoufang/mentougou/ng1hu1nb1/",
    # "https://bj.lianjia.com/ershoufang/pinggu/ng1hu1nb1/",
    # "https://bj.lianjia.com/ershoufang/huairou/ng1hu1nb1/",
    # "https://bj.lianjia.com/ershoufang/miyun/ng1hu1nb1/",
    # "https://bj.lianjia.com/ershoufang/yanqing/ng1hu1nb1/"
]


def getTotals(response):
    xpath_cond = "//h2[contains(concat(' ', normalize-space(@class), ' '), ' total fl ')]/span/text()"
    rst = response.xpath(xpath_cond).extract_first()
    if rst:
        return int(rst.strip())
    return 0


def getHouseInfo(response):
    def getValue(path):
        info = response.xpath(path).extract_first()
        if info:
            info = info.strip()
        return info

    return {
        "链家编号": getValue('//div[@class="aroundInfo"]/div[@class="houseRecord"]/span[@class="info"]/text()'),
        "价格": getValue(
            "//div[contains(concat(' ', normalize-space(@class), ' '), ' price ')]/span[contains(concat(' ', normalize-space(@class), ' '), ' total ')]/text()"),
        "关注": getValue("//span[@id='favCount']/text()"),
        "看过": getValue("//span[@id='cartCount']/text()"),
        "区县": getValue(u"//span[text()='所在区域']/parent::div/span[2]/a[1]/text()"),
        "商圈": getValue(u"//span[text()='所在区域']/parent::div/span[2]/a[2]/text()"),
        "环线": getValue(u"//span[text()='所在区域']/parent::div/span[2]/text()[2]"),
        "小区": getValue('//div[@class="aroundInfo"]/div[@class="communityName"]/a/text()'),
        "房屋户型": getValue(u"//span[text()='房屋户型']/parent::li/text()"),
        "所在楼层": getValue(u"//span[text()='所在楼层']/parent::li/text()"),
        "建筑面积": getValue(u"//span[text()='建筑面积']/parent::li/text()"),
        "户型结构": getValue(u"//span[text()='户型结构']/parent::li/text()"),
        "套内面积": getValue(u"//span[text()='套内面积']/parent::li/text()"),
        "建筑类型": getValue(u"//span[text()='建筑类型']/parent::li/text()"),
        "房屋朝向": getValue(u"//span[text()='房屋朝向']/parent::li/text()"),
        "建筑结构": getValue(u"//span[text()='建筑结构']/parent::li/text()"),
        "装修情况": getValue(u"//span[text()='装修情况']/parent::li/text()"),
        "梯户比例": getValue(u"//span[text()='梯户比例']/parent::li/text()"),
        "供暖方式": getValue(u"//span[text()='供暖方式']/parent::li/text()"),
        "配备电梯": getValue(u"//span[text()='配备电梯']/parent::li/text()"),
        "产权年限": getValue(u"//span[text()='产权年限']/parent::li/text()"),

        "挂牌时间": getValue(u"//span[text()='挂牌时间']/parent::li/span[2]/text()"),
        "上次交易": getValue(u"//span[text()='上次交易']/parent::li/span[2]/text()"),
        "交易权属": getValue(u"//span[text()='交易权属']/parent::li/span[2]/text()"),
        "房屋用途": getValue(u"//span[text()='房屋用途']/parent::li/span[2]/text()"),
        "房屋年限": getValue(u"//span[text()='房屋年限']/parent::li/span[2]/text()"),
        "产权所属": getValue(u"//span[text()='产权所属']/parent::li/span[2]/text()"),
        "抵押信息": getValue(u"//span[text()='抵押信息']/parent::li/span[2]/text()"),
        "房本备件": getValue(u"//span[text()='房本备件']/parent::li/span[2]/text()"),

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
