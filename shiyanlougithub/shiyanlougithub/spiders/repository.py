# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import RepositoryItem

class RepositorySpider(scrapy.Spider):
    name = 'repository'
    start_urls = ['']
    @property
    def start_urls(self):
        url = ('https://github.com/shiyanlou?tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxNiswODowMM4FkpXb&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxNjoxNzo1MyswODowMM4Bx3_0&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yNFQxNTowMDoxNyswODowMM4BnPdj&tab=repositories'
                )
        return url
    def parse(self, response):
        for repository  in response.css('li.public'):
            item = RepositoryItem({
                'name': repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re(r'\n\s*(\w*)'),
                'update_time': repository.xpath('.//relative-time/@datetime').extract_first()
            })
            yield item
