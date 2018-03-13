# -*- coding: utf-8 -*-
import scrapy


class ClassSpider(scrapy.Spider):
    name = 'class'
    allowed_domains = ['http://lyle.smu.edu/~fmoore']
    start_urls = ['http://http://lyle.smu.edu/~fmoore/']

    def parse(self, response):
        pass
