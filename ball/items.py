# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BallItem(scrapy.Item):
    # define the fields for your item here like:
    saishi = scrapy.Field()#赛事
    time = scrapy.Field()#时间
    zhuangtai = scrapy.Field()#状态
    zhuchag = scrapy.Field()#主场球队
    bifen = scrapy.Field()#比分
    kechang = scrapy.Field()#客场球队
    banchang = scrapy.Field()#半场
    jiaoqiu = scrapy.Field()#角球
    zhibo = scrapy.Field()#直播
    zhishu = scrapy.Field()#指数



























