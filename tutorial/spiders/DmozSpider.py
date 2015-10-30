# coding:utf-8
__author__ = 'Administrator'
import sys
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from tutorial.items import DmozItem

reload(sys)
sys.setdefaultencoding('utf-8')


class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.mm131.com",
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        # <ul class="new public-box">
        # <li class="left-list_li"><a target="_blank" href="http://www.mm131.com/xinggan/2236.html">魅妍社新人模特妮可Nicole艺术大</a></li>
        # div class="main_top"
        sites = hxs.select("//div[@class='main_top']/ul/li")
        items = []
        for site in sites:
            title = site.select('a/text()').extract()[0]
            link = site.select('a/@href').extract()[0]
            item = DmozItem()
            item['title'] = title
            item['link'] = link
            items.append(item)
        for item in items:
            print u'标题：', item['title'], u'连接：', item['link']
            print type(item['title']), type(item['link'])
        return items
