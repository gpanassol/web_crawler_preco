# -*- coding: utf-8 -*-
import scrapy


class TecnoblogSpider(scrapy.Spider):
    name = 'Tecnoblog'
    allowed_domains = ['tecnoblog.net']
    start_urls = ['https://tecnoblog.net/']

    def parse(self, response):
        pass
