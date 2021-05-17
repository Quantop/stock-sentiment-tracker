import scrapy
import pandas as pd

class NewsItem(scrapy.Item):
    headline = scrapy.Field()
    link = scrapy.Field()

class NewsSpider(scrapy.Spider):
    name = 'news_spider'
    allowed_domains = ['finviz.com']
    start_urls = ['https://finviz.com/news.ashx']

    def parse(self, response, **kwargs):
        news_items = []
        news_rows = response.xpath('//*[@class="news"]/table//descendant::td[1]//tr')

        for row in news_rows:
            item = NewsItem()
            item['headline'] = row.xpath('td[3]/a/text()')
            item['link'] = row.xpath('td[3]/a/@href')

            news_items.append(item)