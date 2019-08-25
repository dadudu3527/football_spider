# -*- coding: utf-8 -*-
import scrapy
from ball.items import BallItem
from lxml import etree

class LeisuSpider(scrapy.Spider):
    name = 'leisu' #爬虫名字
    allowed_domains = ['live.leisu.com']#爬虫只在该域名下采集数据
    start_urls = ['http://live.leisu.com']#开始采集的网址

    # 解析采集回来的数据
    def parse(self, response):
        pass
