import requests
from bs4 import BeautifulSoup
import lxml.etree
import scrapy
from spider1.items import Spider1Item



class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board']

    def start_requests(self):
        url = 'https://maoyan.com/board'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = []
        soup = BeautifulSoup(response.text, 'html.parser')
        title_list = soup.find_all('p', attrs={'class': 'name'})
        # print(title_list)
        for i in range(len(title_list)):
            item = Spider1Item()
            title = title_list[i].find('a').get('title')
            link = title_list[i].find('a').get('href')
            item['title'] = title
            item['link'] = link
            items.append(item)
        return items

