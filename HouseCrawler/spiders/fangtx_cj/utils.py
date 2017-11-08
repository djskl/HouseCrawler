# coding:utf-8
import math

from scrapy.exporters import CsvItemExporter
from scrapy.conf import settings

COND_QX = ["a01", "a00", "a06", "a02", "a03", "a07", "a012", "a0585", "a010", "a011", "a08", "a013", "a09", "a014", "a015",
           "a016"]

COND_PR = ["c2200-d2300", "c2300-d2400", "c2400-d2500", "c2500-d2800", "c2800-d21000", "c21000-d21500", "c21500-d22000",
           "c22000"]
COND_RM = ["g22", "g23", "g24", "g25", "g299"]
COND_AR = ["j250-k270", "j270-k290", "j290-k2110", "j2110-k2130", "j2130-k2150", "j2150-k2200", "j2200-k2300", "j2300"]

ROOT_URL = "http://esf.fang.com/chengjiao-"
BASE_URLS = [ROOT_URL + qx for qx in COND_QX]

DONES = set()


def getTotals(response):
    xpath_cond = "//b[contains(concat(' ', normalize-space(@class), ' '), ' org ')]/text()"
    rst = response.xpath(xpath_cond).extract_first()

    count, pages = 0, 0

    if rst:
        count = int(rst.strip())
        pages = math.ceil(float(count) / 30)
        pages = pages if pages < 100 else 100

    return count, int(pages)


FIELDS_TO_EXPORT = [
    "日期",
    "户型",
    "价格",
    "面积",
    "小区",
    "商圈",
    "区县",
    "单价",
    "朝向",
    "楼层",
    "链接"
]


class HouseCsvExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        delimiter = settings.get('CSV_DELIMITER', ',')
        kwargs['delimiter'] = delimiter
        kwargs['fields_to_export'] = FIELDS_TO_EXPORT
        super(HouseCsvExporter, self).__init__(*args, **kwargs)
