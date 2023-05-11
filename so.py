import scrapy
import pandas as pd


start_urls = 'https://stackoverflow.com/questions/tagged/{}'

# reading the csv file which have acolumn that have the names of programming languages
def read_csv():
    df = pd.read_csv('data_file.csv')
    return df['Tags'].values.tolist()


class SoSpider(scrapy.Spider):
    name = 'so'

    def start_requests(self):
        for tag in read_csv():
            yield scrapy.Request(start_urls.format(tag))

    def parse(self, response):
        questions = response.css('.sm\:mb12::text').get()

        yield {
            'questions': questions,
            'url': response.url
        }
