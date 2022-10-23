import scrapy
import requests

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        proxies = {'http': 'http://51.255.115.229:1080'}
        urls = [
            #'https://www.leboncoin.fr/recherche/?category=35&text=bordeaux%20paris',
            'https://whatismyipaddress.com/fr/mon-ip'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'proxy':'http://51.255.115.229:1080'})

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'lbc-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
