import scrapy
from selenium import webdriver
from scrapy.http import HtmlResponse
import time

class JavaScriptMiddleware(object):
    def process_request(self, request, spider):
        print('--------------Firefox is starting--------------')
        driver = spider.driver
        driver.get(request.url)
        if request.url == 'https://www.zhihu.com/':
            login = driver.find_element_by_xpath("//a[@href='#signin']")
            time.sleep(2)
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
                driver.find_element_by_css_selector('button.sign-button.submit').click()
        else:
            """
            private coding
            """
            for i in range(20):
                button_more = driver.find_element_by_css_selector('a.zg-btn-white.zu-button-more')
                button_more.click()
                time.sleep(2)
            time.sleep(10)
            print('---------------Login is ending---------------')
        print('---------------Firefox is ending---------------')
        return HtmlResponse(url=driver.current_url, body=driver.page_source, encoding='utf-8', request=request)
