import scrapy
import lxml.etree
from proxyspider.items import ProxyspiderItem


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    # 通过IP查看请求的ip地址
    start_urls = ['http://httpbin.org/ip']
    # 通过header查看user-agent
    # start_urls = ['http://httpbin.org/header']

    
    def parse(self, response):
        items = []
        item = ProxyspiderItem()
        item['ipaddr'] = response.text
        items.append(item)
        return items
