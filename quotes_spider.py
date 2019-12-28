import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import QuotetutorialItem
class Quotespider(scrapy.Spider):# have to inherit from scrapy.Spider class
    name = 'quotes'  #name - of our crawler and start_urls should not change. Must remain intact
    page_number =  2
    start_urls =[
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'ishan@gmail.com',
            'password': 'adasd'
        }, callback = self.start_scraping)
    def start_scraping(self,response):
        open_in_browser(response)
        items = QuotetutorialItem()
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items

