import scrapy
from ..items import BookspiderItem
class Book(scrapy.Spider):
    name = "BookSpider"
    start_urls = [
        'http://www.xbiquge.la/xiaoshuodaquan/'
    ]

    def parse(self, response):
        bookAllList = response.css('.novellist:first-child>ul>li')

        for all in bookAllList:
            booklist = all.css('a::attr(href)').extract_first()
            yield scrapy.Request(booklist,callback=self.list)

    def list(self,response):
        book_name = response.css('#info>h1::text').extract_first()
        book_img = response.css('#fmimg>img::attr(src)').extract_first()
        book_author = response.css('#info p:nth-child(2)::text').extract_first()
        book_last_chapter = response.css('#info p:last-child::text').extract_first()
        book_last_time = response.css('#info p:nth-last-child(2)::text').extract_first()
        bookInfo = {
            'book_name':book_name,
            'book_img':book_img,
            'book_author':book_author,
            'book_last_chapter':book_last_chapter,
            'book_last_time':book_last_time
        }
        list = response.css('#list>dl>dd>a::attr(href)').extract()
        i = 0
        for var in list:
            i += 1
            bookInfo['i'] = i # 获取抓取时的顺序，保存数据时按顺序保存
            yield scrapy.Request('http://www.xbiquge.la'+var,meta=bookInfo,callback=self.info)

    def info(self,response):
        self.log(response.meta['book_name'])
        content = response.css('#content::text').extract()
        item = BookspiderItem()
        item['i'] = response.meta['i']
        item['book_name'] = response.meta['book_name']
        item['book_img'] = response.meta['book_img']
        item['book_author'] = response.meta['book_author']
        item['book_last_chapter'] = response.meta['book_last_chapter']
        item['book_last_time'] = response.meta['book_last_time']
        item['book_list_name'] = response.css('.bookname h1::text').extract_first()

        item['book_content'] = ''.join(content)
        yield item

