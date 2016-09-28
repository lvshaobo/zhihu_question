import scrapy
from selenium import webdriver
from scrapy.http import HtmlResponse
import time
from log import Logger

class JavaScriptMiddleware(object):
    log = Logger(__name__)
    def process_request(self, request, spider):
        self.log.info('start_browser')
        driver = spider.driver
        driver.get(request.url)
        time.sleep(2)
        if request.url == 'https://www.zhihu.com/':
            self.log.info('start_login')
            login = driver.find_element_by_xpath("//a[@href='#signin']")
            login.click()
            account = driver.find_element_by_name('account')
            password = driver.find_element_by_name('password')
            account.send_keys('lvshaoboftd@163.com')
            password.send_keys('root2007')
            """
            # driver.maximize_window()
            # driver.set_window_size(800,600)
            # driver.save_screenshot('output/login.png')
            """
            print('Please Enter Password')
            ch = input()
            if ch:
                time.sleep(2)
                submit = driver.find_element_by_css_selector('button.sign-button.submit')
                submit.click()
                self.log.info('end_login')
        else:
            """
            private coding
            """
            self.log.info('start_question')
            for i in range(20):
                button_more = driver.find_element_by_css_selector('a.zg-btn-white.zu-button-more')
                button_more.click()
                time.sleep(1)
            self.log.info('end_question')
        self.log.info('end_browser')
        return HtmlResponse(url=driver.current_url, body=driver.page_source, encoding='utf-8', request=request)
