# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from redis import Redis
class BallPipeline(object):
    def process_item(self, item, spider):
        r= Redis(host='127.0.0.1',port=6379,db=10)

        return item
