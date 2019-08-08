

import scrapy


class BookspiderItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    book_img = scrapy.Field()
    book_author = scrapy.Field()
    book_last_chapter = scrapy.Field()
    book_last_time = scrapy.Field()
    book_list_name = scrapy.Field()
    book_content = scrapy.Field()
    pass
