# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import RepositoryItem


class RepositorySpider(scrapy.Spider):
    name = 'repository'
    start_urls = ['https://github.com/shiyanlou?tab=repositories']

    def parse(self, response):
        for repository in response.css('li.public'):
            item = RepositoryItem()
            item['name'] = repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re(r'\n\s*(.*)')
            item['update_time'] = repository.xpath('.//relative-time/@datetime').extract_first()
            repo_url = response.urljoin(repository.xpath('.//a/@href').extract_first())
            request = scrapy.Request(repo_url,callback=self.parse_repo)
            request['item'] = item
            yield request
        for url in response.xpath('//div[@class="paginate-container"]/a/@href'):
            yield request.fllow(url=,callback=parse)

    def parse_repo(self,reponse):
        for i in reponse.css('ul.numbers-summary'):
            item = reponse.meta['item']
            item['commits'] = i.xpath('')
            item['branches'] = i.xpath('')
            item['releases'] = 
