# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.http import FormRequest
from zhihu.items import ZhihuItem
from bs4 import BeautifulSoup
from script import txt_dict
from script import header_dict
import time

import logging

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logger.info('foorbar')


class ZhihuQuesionSpider(scrapy.Spider):
    name = "zhihu.question"
    allowed_domains = ["zhihu.com"]
    """
    start_urls = (
        'http://www.zhihu.com',
    )
    """
    # cookies = txt_dict.txt_dict('script/Cookie')
    headers = header_dict.header_dict('script/Header')

    def start_requests(self):
        print('****************start_requrest***************')
        yield Request(url='https://www.zhihu.com/',
                             headers = self.headers,
                             meta = {'cookiejar': 1},
                             callback=self.request_captcha)
    
    def request_captcha(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        print('----------------request_captcha---------------')
        xsrf = soup.find_all('input', {'name': '_xsrf'})[-1]['value']
        #xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
        print(type(xsrf))
        print(xsrf)
        print(time.time()*1000)
        captcha_url = "http://www.zhihu.com/captcha.gif?r=" + str(time.time()*1000) + '&type=login'
        yield Request(url=captcha_url,
                             headers=self.headers,
                             meta={"cookiejar": response.meta["cookiejar"],
                                   "_xsrf": xsrf},
                             callback=self.post_login)
    
    
    def post_login(self, response):
        print('-------------------post_login------------------')
        with open("output/captcha.gif", "wb") as fp:
            fp.write(response.body)
        print("请输入验证码: ")
        captcha = input()
        yield FormRequest(url='https://www.zhihu.com/login/email',
                                 headers=self.headers,
                                 formdata={"email": 'lvshaoboftd@163.com',
                                           "password": 'LVshaobo',
                                           "_xsrf": response.meta["_xsrf"],
                                           "remember_me": "true",
                                           "captcha": captcha},
                                 meta={"cookiejar": response.meta["cookiejar"],},
                                 callback=self.request_question)

    
    def request_question(self, response):
        print('-----------------request_question----------------')
        yield Request(url='https://www.zhihu.com/',
                      meta={'cookiejar': response.meta['cookiejar']},
                      callback=self.parse,
                      dont_filter=True)
    
    
    def parse(self, response):
        print('----------------------parse---------------------')
        html_doc = response.body
        soup = BeautifulSoup(html_doc, 'lxml')
        filename = 'output/zhihu.question'
        with open(filename, 'wb') as f:
            f.write(response.body)
        item = ZhihuItem()
        item['title'] = soup.title.string
        item['question'] = soup.find_all('a', class_='question_link')
        item['corp'] = soup.find_all('span', class_='corp')
        return item
