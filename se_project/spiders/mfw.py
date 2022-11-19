'''
/*: 
* Author: OBKoro1
* Date: 2019-09-24 20:25:33
LastEditors: Please set LastEditors
LastEditTime: 2022-11-19 14:11:14
* FilePath: /fileHead/test.js
'''
import scrapy


class MfwSpider(scrapy.Spider):
    name = 'mfw'
    allowed_domains = ['www.mfw.com']
    start_urls = ['https://www.mafengwo.cn/hotel/8299351.html?iMddid=10099',
                  'https://www.mafengwo.cn/hotel/4532.html?iMddid=10099']

    # def start_request(self):
    #     url = ""
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True, meta={'page': '0'})

    def parse(self, response):
        table = response.xpath("//div[@id='_j_comment_list']/div")
        for it in table:
            comment = it.xpath("./div[2]/text()").get()
            print(comment)
            print("="*30)
        
        # 判断是否有下一页
        # next = response.xpath("//a[text()='下一页 >>']")
        # print("next:",next,len(next))
        # if len(next) != 0:
        #     yield scrapy.Request(response.url,callback=self.parse,meta={"page":'2'})


