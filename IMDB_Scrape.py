import scrapy


class ImdbScrapeSpider(scrapy.Spider):
    name = "IMDB_Scrape"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top"]
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=headers)
    def parse(self, response):
        movies = response.css("ipc-metadata-list-summary-item__c")
        for movie in movies:
            yield{

                "Titles": movie.css("h3::text").get().split(". ")[1],
                "Imdb ratings": movie.css(".ipc-rating-star span::text").get(),
                "Release Year" : movie.css(".cli-title-metadata span::text").get(),
            }
