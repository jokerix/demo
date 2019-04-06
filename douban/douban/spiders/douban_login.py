# -*- coding: utf-8 -*-
import scrapy
from urllib import request
from PIL import Image


class DoubanLoginSpider(scrapy.Spider):
    name = 'douban_login'
    allowed_domains = ['douban.com']
    start_urls = ['http://accounts.douban.com/login']
    login_url = 'http://accounts.douban.com/login'
    profile_url = 'http://accounts.douban.com/j/people/97956064'

    editsignature_url = 'http://accounts.douban.com/j/people/97956064/edit_signature'

    def parse(self, response):
        formdata = {
            'source': 'None',
            'redir': 'https://www.douban.com/',
            'form-email': '970138074@qq.com',
            'form_password': 'pythonspider',
            'remeber': 'on',
            'login': '登录'

        }
        captcha_url = response.css('img#captcha_image::attr(src)').get()
        if captcha_url:
            captcha = self.recoginze_captcha(captcha_url)
            formdata['captcha-solution'] = captcha
            captcha_id = response.xpath("//input[@name= 'captcha-id']/@value").get()
            formdata['captcha-id'] = captcha_id
            yield scrapy.FormRequest(url=self.login_url, formdata=formdata, callback=self.parse_after_login)

    def parse_after_login(self, response):
        if response.url == 'https://www.douban.com/':
            yield scrapy.Request(self.profile_url, callback=self.parse_profile)
            print('登录成功')
        else:
            print('失败')

    def parse_profile(self, response):
        print(response.url)
        if response.url == self.profile_url:
            ck = response.xpath("//input[@name= 'ck']/@value").get()
            formdata = {
                'ck': ck,
                'signature': 'keyi '

            }
            yield scrapy.FormRequest(self.editsignature_url, formdata=formdata, callback=self.parse_none)

        else:
            print('no')

    def parse_none(self, response):
        pass

    def recoginze_captcha(self, image_url):
        request.urlretrieve(image_url, 'captcha.png')
        image = Image.open('capacha.png')
        image.show()
        captcha = input('shuru ')
        return captcha


from base64 import b64decode


def recoginze_captcha(self, image_url):
    recognize_url = image_url
    formdata = {}
    with open('captcha.png', 'rb')as fp:
        data = fp.read()
        pic = b64decode(data)
        formdata['pic'] = pic
    appcode = ''
    headers = {
        "Content-Type": '',
        'Authorization': 'APPCODE' + appcode

    }

    response = request.post(recognize_url, data=formdata, headers=headers)
    result = response.json()
    code = result['result']['code']
    return code
