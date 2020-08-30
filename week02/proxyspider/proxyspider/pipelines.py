# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class ProxyspiderPipeline:
    def __init__(self):
        self.conn = pymysql.connect('localhost',3306,'root','loly1234','test')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        sqls = ['insert into iptables(ipaddr) VALUES(%s)']
        self.cur.execute(sqls,(item['ipaddr']))
        # ipaddr = item['ipaddr']
        # output = f'{ipaddr}'
        # with open('./ip_addr.txt', 'a+', encoding='utf-8') as ip_list:
        #     ip_list.write(output)
        #     ip_list.close()
        # return item
        self.conn.commit()

    def closedb(self, spider):
        self.cur.close()
        self.conn.close()
        