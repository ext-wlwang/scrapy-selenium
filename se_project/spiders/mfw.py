'''
/*: 
* Author: OBKoro1
* Date: 2019-09-24 20:25:33
LastEditors: Please set LastEditors
LastEditTime: 2022-11-19 14:11:14
* FilePath: /fileHead/test.js
'''
import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import MfwItem


class MfwSpider(RedisSpider):
    name = 'mfw'
    allowed_domains = ['www.mfw.com']
    # start_urls = ['https://www.mafengwo.cn/hotel/8299351.html?iMddid=10099']
    redis_key = 'mfw:start_urls'

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url, callback=self.parse, dont_filter=True, meta={'page': '0'})

    def parse(self, response):
        table = response.xpath("//div[@id='_j_comment_list']/div")
        for it in table:
            item = MfwItem()
            item['comment'] = it.xpath("./div[2]/text()").get()
            yield item
            
        
        


