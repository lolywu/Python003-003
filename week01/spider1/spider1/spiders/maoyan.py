import requests
from bs4 import BeautifulSoup
import lxml.etree
import scrapy
from spider1.items import Spider1Item



class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com']

    def start_requests(self):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        headers = {}
        headers['user-agent'] = user_agent
        myurl1 = 'https://maoyan.com/board'
        response1 = requests.get(myurl1, headers=headers)
        response1.encoding='utf-8'
        soup = BeautifulSoup(response1.text, 'html.parser')
        title_list = soup.find_all('p', attrs={'class': 'name'})
        for i in range(len(title_list)):
            link = ('https://maoyan.com'+title_list[i].find('a').get('href'))
            yield scrapy.Request(url=link, callback=self.parse)

    def parse(self, response):
        items = []
        item = Spider1Item()
        selector = lxml.etree.HTML(response.text)
        film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/div/text()')
        film_type = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[1]/text()')
        plan_date = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
            
        item['title'] = film_name
        item['link'] = film_type
        item['time'] = plan_date
        
        items.append(item)
        return items