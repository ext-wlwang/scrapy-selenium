# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from scrapy.http import HtmlResponse
import random
import time


class SeProjectSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SeProjectDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class seleniumDownloaderMiddleware:
    def __init__(self):
        # options = webdriver.ChromeOptions()
        # # options.add_argument('--headless')
        # self.driver = webdriver.Chrome(chrome_options=options)
        # # 设置20秒页面超时返回
        # self.driver.set_page_load_timeout(180)
        # # 设置20秒脚本超时时间
        # self.driver.set_script_timeout(180)
        self.driver = Remote(
            command_executor="http://192.168.10.152:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.CHROME,
        )
        self.driver.maximize_window()
    
    def random_time(self):
        '''
        TODO:设置随机等待时间
        '''
        timeout = random.randint(1,3) + random.random()
        time.sleep(timeout)
        
        



    
    
    def process_request(self, request, spider):
        self.driver.get(request.url)
        self.random_time()
        count = 0
        body = ''
        nextbund = True
        while nextbund:
            body = body + self.driver.page_source
            count += 1
            print("=" * 30,count,len(body))
            self.random_time()
            # 判断是否又点击按钮
            page = self.driver.find_elements(By.XPATH,"//a[text()='下一页 >>']")
            if len(page) != 0:
                self.driver.find_element(By.XPATH,"//a[text()='下一页 >>']").send_keys(Keys.ENTER)
                self.random_time()
                # return HtmlResponse(self.driver.current_url, body=self.driver.page_source,y, encoding='utf-8', request=request)
            else:
                nextbund = False
        print(len(body))
        
        return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)
    
    def spider_closed(self):
        self.driver.quit()