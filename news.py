import scrapy
import pandas as pd

class NewsSpider(scrapy.Spider):
    name = 'news_spider'
    allowed_domains = ['finviz.com']
    start_urls = ['https://finviz.com/news.ashx']

    def parse(self, response, **kwargs):
        self.logger.info(response.xpath('//a[@class="nn-tab-link"]'))