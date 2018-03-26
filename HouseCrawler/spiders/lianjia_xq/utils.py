# coding:utf-8
from scrapy.conf import settings
from scrapy.exporters import CsvItemExporter

def getHouseInfo(response):
    house_info = {
        "链家编号": response.xpath(u"//span[text()='链家编号']/parent::li/text()").extract_first(),
        "小区名称": response.xpath(u"//div[contains(@class, 'house-title')]/div/text()").extract_first().split(" ")[0],
        "成交日期": response.xpath(u"//div[contains(@class, 'house-title')]/div/span/text()").extract_first().split(" ")[0],
        "成交价格": response.xpath(u"//span[@class='dealTotalPrice']/i/text()").extract_first(),
        "挂牌价格": response.xpath(u"//span[text()='挂牌价格（万）']/label/text()").extract_first(),
        "成交周期": response.xpath(u"//span[text()='成交周期（天）']/label/text()").extract_first(),
        "调价次数":response.xpath(u"//span[text()='调价（次）']/label/text()").extract_first(),
        "带看次数":response.xpath(u"//span[text()='带看（次）']/label/text()").extract_first(),
        "关注人数":response.xpath(u"//span[text()='关注（人）']/label/text()").extract_first(),
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
        "链接": response.url
    }

    for fn in house_info:
        if house_info[fn]:
            house_info[fn] = house_info[fn].strip()

    return house_info


FIELDS_TO_EXPORT = [
    "链家编号",
    "小区名称",
    "成交价格",
    "挂牌价格",
    "成交日期",
    "成交周期",
    "调价次数",
    "带看次数",
    "关注人数",
    "房屋户型",
    "所在楼层",
    "建筑面积",
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
    "挂牌时间",
    "上次交易",
    "交易权属",
    "房屋用途",
    "房屋年限",
    "产权所属",
    "链接",
]


class HouseCsvExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        delimiter = settings.get('CSV_DELIMITER', ',')
        kwargs['delimiter'] = delimiter
        kwargs['fields_to_export'] = FIELDS_TO_EXPORT
        super(HouseCsvExporter, self).__init__(*args, **kwargs)


BASE_URLS = [
    "https://bj.lianjia.com/chengjiao/anningzhuang1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/aolinpikegongyuan11/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/baishiqiao1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/beitaipingzhuang/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/changpingqita1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/changwa/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/dinghuisi/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/erlizhuang/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/gongzhufen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/ganjiakou/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/haidianqita1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/haidianbeibuxinqu1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/junbo1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/liuliqiao1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/madian1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/mudanyuan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/malianwa/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/qinghe11/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/suzhouqiao/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shijicheng/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/sijiqing/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shuangyushu/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shangdi1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/tiancun1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/wanshoulu1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/weigongcun/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/wukesong1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/wanliu/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/wudaokou/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xiaoxitian1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xibeiwang/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xinjiekou2/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xizhimen1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xisanqi1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xishan21/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xueyuanlu1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xierqi1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yiheyuan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yuquanlu11/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yangzhuang1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yuanmingyuan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/zaojunmiao/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/zizhuqiao/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/zhongguancun/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/zhichunlu/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/andingmen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/baizhifang1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/caihuying/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/changchunjie/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/chongwenmen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/chegongzhuang1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/dianmen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/deshengmen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/fuchengmen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/guanganmen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/guanyuan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/jinrongjie/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/liupukang/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/madian1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/maliandao1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/muxidi1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/niujie/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/taoranting1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/tianningsi1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xisi1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xuanwumen12/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xizhimen1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xinjiekou2/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xidan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yuetan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/youanmennei11/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/beidadi/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/beijingnanzhan1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/chengshousi1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/caoqiao/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/caihuying/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/dahongmen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/fengtaiqita1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/fangzhuang1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/guanganmen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/heyi/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/huaxiang/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/jiugong1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/jiaomen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/kejiyuanqu/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/kandanqiao/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/lize/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/liujiayao/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/lugouqiao1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/liuliqiao1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/muxiyuan1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/majiabao/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/maliandao1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/puhuangyu/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/qingta1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/qilizhuang/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/songjiazhuang/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shilihe/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/taipingqiao1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/wulidian/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xihongmen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xiluoyuan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xingong/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yuegezhuang/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yuquanying/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/youanmenwai/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yangqiao1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/zhaogongkou/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/bajiao1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/chengzi/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/gucheng/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/laoshan1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/lugu1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/pingguoyuan1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shijingshanqita1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yangzhuang1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yuquanlu11/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/andingmen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/anningzhuang1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/aolinpikegongyuan11/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/baishanzhen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/beiqijia/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/changpingqita1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/dongguan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/guloudajie/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/huilongguan2/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/huoying/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/lishuiqiao1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/nankou/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/nanshao/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shahe2/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/tiantongyuan1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/anzhen1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/aolinpikegongyuan11/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/beiyuan2/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/beigongda/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/baiziwan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/chengshousi1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/changying/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/chaoyangmenwai1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/cbd/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/chaoqing/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/chaoyanggongyuan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/dongzhimen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/dongba/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/dawanglu/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/dongdaqiao/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/dashanzi/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/dougezhuang/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/dingfuzhuang/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/fangzhuang1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/fatou/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/guangqumen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/gongti/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/gaobeidian/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/guozhan1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/ganluyuan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/guanzhuang/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/hepingli/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/huanlegu/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/huixinxijie/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/hongmiao/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/huaweiqiao/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/jianxiangqiao1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/jiuxianqiao/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/jinsong/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/jianguomenwai/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/lishuiqiao1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/madian1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/nongzhanguan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/nanshatan1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/panjiayuan1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/sanyuanqiao/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shaoyaoju/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shifoying/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shilibao/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shoudoujichang1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shuangjing/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shilihe/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shibalidian1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shuangqiao/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/sanlitun/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/sihui/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/tongzhoubeiyuan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/tuanjiehu/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/taiyanggong/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/tianshuiyuan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/wangjing/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xibahe/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yayuncun/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yayuncunxiaoying/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yansha1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/zhongyangbieshuqu1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/zhaoyangqita/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xiguanhuandao/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xisanqi1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xiaotangshan1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/daxingqita11/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/guanyinsi/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/heyi/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/huangcunhuochezhan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/huangcunbei/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/huangcunzhong/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/jiugong1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/kejiyuanqu/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/tiangongyuan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xihongmen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yizhuang1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/zaoyuan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/majuqiao1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yizhuang1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yizhuangkaifaquqita1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/pingguqita1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/houshayu1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/liqiao1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/mapo/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shunyicheng/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shunyiqita1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shoudoujichang1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/tianzhu1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/zhongyangbieshuqu1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/binhexiqu1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/chengzi/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/dayu/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/fengcun/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/mentougouqita1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shimenying/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shijingshanqita1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/chengguan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/changyang1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/doudian/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/fangshanqita/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/hancunhe1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/liangxiang/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/liulihe/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yancun/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yanshan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/miyunqita11/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yanqingqita1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/huairouchengqu1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/huairouqita1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/andingmen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/anzhen1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/chaoyangmenwai1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/chaoyangmennei1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/chongwenmen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/dongdan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/dongzhimen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/dianmen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/donghuashi/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/dongsi1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/dengshikou/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/guangqumen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/gongti/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/hepingli/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/jiaodaokou/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/jianguomenwai/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/jianguomennei/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/jinbaojie/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/liupukang/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/puhuangyu/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/qianmen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/taoranting1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/tiantan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xiluoyuan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xidan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yongdingmen/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/zuoanmen1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/beiguan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/guoyuan1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/jiukeshu12/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/luyuan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/liyuan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/linheli/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/majuqiao1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/qiaozhuang/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/shoudoujichang1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/tongzhoubeiyuan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/tongzhouqita11/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/wuyihuayuan/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/xinhuadajie/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yizhuang1/ng1hu1nb1",
    "https://bj.lianjia.com/chengjiao/yuqiao/ng1hu1nb1"
]