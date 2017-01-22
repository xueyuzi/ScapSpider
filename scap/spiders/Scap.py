# -*- coding: utf-8 -*-
import scrapy
from scap.items import ScapItem

class ScapSpider(scrapy.Spider):
    name = "Scap"
    allowed_domains = ["cve.scap.org.cn"]
    start_urls = ['http://cve.scap.org.cn/cve_list.php']

    def parse(self, response):
    	item = ScapItem()
    	item['time'] = response.xpath("//div[@class='entry']/h2/span[2]/text()").extract()
    	item['name'] = response.xpath("//div[@class='entry']/h2/span/a/text()").extract()
    	return item
