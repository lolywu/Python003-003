#安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
import requests
from bs4 import BeautifulSoup as bs
import csv
import lxml.etree
import pandas as pd


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
headers = {}
headers['user-agent'] = user_agent

myurl1 = 'https://maoyan.com/board'
response1 = requests.get(myurl1, headers=headers)
response1.encoding='utf-8'

# print(response1.text)
bs_info = bs(response1.text, 'html.parser')

for tag in bs_info.find_all('p', attrs={'class': 'name'}):
    for atag in tag.find_all('a',):
        urls = ('https://maoyan.com'+atag.get('href'))
        # print('-----------------------------------------', urls)
        response2 = requests.get(urls, headers=headers)
        response2.encoding='utf-8'
        selector = lxml.etree.HTML(response2.text)
        film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/div/text()')
        #print(f'moviename: {film_name}')
        film_type = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[1]/text()')
        #print(f'movietype: {film_type}')
        plan_date = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
        #print(f'movietime: {plan_date}')
        mylist = [film_name, film_type, plan_date]
        with open('./极客/1stWeek-requests-Scrapy/movie1.csv', 'a', newline='') as csvfile:
            writer  = csv.writer(csvfile)
            writer.writerow(mylist)

# movie1 = pd.DataFrame(data = mylist)
# movie1.to_csv('./极客/1stWeek-requests-Scrapy/movie1.csv', encoding='utf-8', index=False, header=False)