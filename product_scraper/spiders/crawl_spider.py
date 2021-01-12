# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from product_scraper.items import Data


class ScrapyParsing(CrawlSpider):
    name = 'crawl_spider'
    allowed_domains = ['imdb.com']
    url = 'https://www.imdb.com/search/title/'
    check = False
    count = int(input("Введите в первый раз как увидете сообщение цифру 1 и нажмите Enter во второй раз введите 0: "))
    if count != 1:
        while not check:
            title = str(input("Введите название фильма или оставьте поле пустым: "))
            title = title.replace(" ", "+")
            url = url + '?title=' + title
            title_type = int(input("Введите 1 чтобы выбрать Title Type или 0 чтобы пропустить: "))

            if title_type != 0:
                url = url + '&title_type='
                response = int(input("Чтобы выбрать Feature Film введите 1, далее - 0: "))
                if response != 0:
                    url = url + 'feature,'
                response = int(input("Чтобы выбрать TV Movie введите 1, далее - 0: "))
                if response != 0:
                    url = url + 'tv_movie,'
                response = int(input("Чтобы выбрать TV Series введите 1, далее - 0: "))
                if response != 0:
                    url = url + 'tv_series,'
                response = int(input("Чтобы выбрать  TV Episode введите 1, далее - 0: "))
                if response != 0:
                    url = url + 'tv_episode,'
                response = int(input("Чтобы выбрать TV Special введите 1, далее - 0: "))
                if response != 0:
                    url = url + 'tv_special,'
                response = int(input("Чтобы выбрать Mini-series введите 1, далее - 0: "))
                if response != 0:
                    url = url + 'tv_miniseries,'
                response = int(input("Чтобы выбрать Video game введите 1, далее - 0: "))
                if response != 0:
                    url = url + 'video_game,'
                response = int(input("Чтобы выбрать Short введите 1, далее - 0: "))
                if response != 0:
                    url = url + 'short,'

            release_date = int(input("Введите 1 чтобы выбрать Release date или 0 чтобы пропустить: "))
            if release_date != 0:
                url = url + '&release_date='
                url_release_date = str(input("Введите начальную дату в формате YYYY-MM-DD: "))
                url = url + url_release_date + ","
                url_release_date = str(input("Введите конечную дату в формате YYYY-MM-DD: "))
                url = url + url_release_date

            release_date = int(input("Введите 1 чтобы выбрать User Rating или 0 чтобы пропустить: "))
            if release_date != 0:
                url = url + '&user_rating='
                url_rating = str(input("Введите минимальный рейтинг в диапазоне 1.0 - 10.0: "))
                url = url + url_rating + ","
                url_rating = str(input("Введите максимальный рейтинг в диапазоне 1.0 - 10.0: "))
                url = url + url_rating

            genres = int(input("Введите 1 чтобы выбрать Genre или 0 чтобы пропустить: "))
            if genres != 0:
                url = url + '&genres='
                response = int(input("Чтобы выбрать Action введите 1, далее - 0: "))
                if response != 0:
                    url = url + 'action,'
                response = int(input("Чтобы выбрать adventure введите 1, далее - 0: "))
                if response != 0:
                    url = url + 'adventure,'
                response = int(input("Чтобы выбрать comedy введите 1, далее - 0: "))
                if response != 0:
                    url = url + 'comedy,'
                response = int(input("Чтобы выбрать history введите 1, далее - 0: "))
                if response != 0:
                    url = url + 'history,'
                response = int(input("Чтобы выбрать horror введите 1, далее - 0: "))
                if response != 0:
                    url = url + 'horror,'
                response = int(input("Чтобы выбрать thriller введите 1, далее - 0: "))
                if response != 0:
                    url = url + 'thriller,'
                response = int(input("Чтобы выбрать war введите 1, далее - 0: "))
                if response != 0:
                    url = url + 'war,'

            check = True
    start_urls = [url]
    rules = (
        Rule(LinkExtractor(allow=('https://www.imdb.com/title/',)), callback='parsing'),
    )

    def parsing(self, response):
        item = Data()
        item['url_movie'] = response.url
        item['name'] = response.xpath("//div[@class='title_wrapper']/h1/text()").get()
        item['genre'] = response.xpath("//div[@class='subtext']/a[position()<last()]/text()").extract()
        item['rate'] = response.xpath("//span[@itemprop='ratingValue']/text()").get()
        item['stars'] = response.xpath("//div[@class='plot_summary ']/div[@class='credit_summary_item'][3]/a[position()<last()]/text()").extract()
        item['Country'] = response.xpath("//div[@id='titleDetails']/div[@class='txt-block'][./h4/text()='Country:']/a/text()").extract()
        item['Language'] = response.xpath("//div[@id='titleDetails']/div[@class='txt-block'][./h4/text()='Language:']/a/text()").extract()
        item['Budget'] = response.xpath("//div[@id='titleDetails']/div[@class='txt-block'][./h4/text()='Budget:']/text()").extract()
        item['Sound'] = response.xpath("//div[@id='titleDetails']/div[@class='txt-block'][./h4/text()='Sound Mix:']/a/text()").extract()
        item['Ratio'] = response.xpath("//div[@id='titleDetails']/div[@class='txt-block'][./h4/text()='Aspect Ratio:']/text()").extract()
        return item
