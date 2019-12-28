import scrapy
from ..items import QuotetutorialItem
class Quotespider(scrapy.Spider):# have to inherit from scrapy.Spider class
    name = 'quotes'  #name - of our crawler and start_urls should not change. Must remain intact
    page_number =  2
    start_urls =[
        'http://quotes.toscrape.com/page/2/'
    ]

    def parse(self, response):
        items = QuotetutorialItem()
        all_div_quotes = response.css('div.quote')


        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] =title
            items['author'] = author
            items['tag'] = tag

            yield items # yiled help in returning as dictionary a key values pair

        #next_page = response.css('li.next a::attr(href)').get() #to extract 'next page process'
        next_page = 'http://quotes.toscrape.com/page/'+str(Quotespider.page_number)+'/'
        #print(next_page)
        #if next_page is not None:
         #   yield response.follow(next_page,callback=self.parse)
        if Quotespider.page_number < 11:
            Quotespider.page_number += 1
            yield response.follow(next_page,callback=self.parse)

