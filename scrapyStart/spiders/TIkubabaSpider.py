from scrapy import Request
from scrapy.spider import Spider

class TikubabaSpider(Spider):
    name = "tikubaba"
    allowed_domains = ["tikubaba.com"]

    start_urls = ["http://www.tikubaba.com/"]


    def parse(self, response):
        chapterUrls = response.xpath('//div[@id="search_main"]/div[2]/table//span/a/@href').extract()

        for chapterUrl in chapterUrls:
            yield Request(chapterUrl, callback=self.parseChapter)


    def parseChapter(self, response):
        questionUrls = response.xpath('//div[@id="ProDiv"]/div[@class="ProInfo"]//a/@href').extract()
        for questionUrl in questionUrls:
            yield Request(questionUrl, callback=self.parseQuestion)


    def parseQuestion(self, response):
        html = response.body
        url = response.url
        utf8Html = html.decode('gb2312', 'ignore')
        try:
            file = open("F:\\tikubaba.html", 'w')
            file.write(str(utf8Html))
        finally:
            if file:
                file.close()
