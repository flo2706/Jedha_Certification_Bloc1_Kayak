import logging
import scrapy
from scrapy.crawler import CrawlerProcess
import os

class HotelsSpider(scrapy.Spider):
    name = "hotels_description"

    locations = [
        "Le+Mont-Saint-Michel", "Saint-Malo", "Bayeux", "Le+Havre", "Rouen", "Paris", "Amiens",
        "Lille", "Strasbourg", "Chateau+du+Haut+Koenigsbourg", "Colmar", "Eguisheim", "Besancon",
        "Dijon", "Annecy", "Grenoble", "Lyon", "Gorges+du+Verdon", "Bormes+les+Mimosas", "Cassis",
        "Marseille", "Aix+en+Provence", "Avignon", "Uzes", "Nîmes", "Aigues+Mortes",
        "Saintes+Maries+de+la+mer", "Collioure", "Carcassonne", "Ariege", "Toulouse",
        "Montauban", "Biarritz", "Bayonne", "La+Rochelle"
    ]

    start_urls = [f"https://www.booking.com/searchresults.fr.html?ss={location}" for location in locations]

    def parse(self, response):
        location = response.url.split("ss=")[-1].replace("+", " ")
        hotels = response.css('div[data-testid="property-card"]')

        for hotel in hotels:
            name = hotel.css('div[data-testid="title"]::text').get()
            url = hotel.css('a[data-testid="title-link"]::attr(href)').get()
            rating = hotel.css("div[class='a3b8729ab1 d86cee9b25']::text").get()

            if url:
                # Follow the hotel link and pass metadata to next parser
                yield response.follow(
                    url,
                    callback=self.parse_hotel,
                    meta={
                        'location': location,
                        'name': name.strip() if name else None,
                        'rating': rating
                    }
                )

    def parse_hotel(self, response):
        description = response.css('p[data-testid="property-description"]::text').get()
     
        coord = response.xpath('//*[@data-atlas-latlng]/@data-atlas-latlng').get()
        

        yield {
            'location': response.meta['location'],
            'name': response.meta['name'],
            'rating': response.meta['rating'],
            'url': response.url,
            'description': description.strip() if description else None,
            'coordinates': coord
        }

filename = "hotels_descriptions.json"

# Delete the file if it already exists to avoid appending
if os.path.exists(filename):
    os.remove(filename)

# Configure and start the Scrapy process
process = CrawlerProcess(settings={
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'LOG_LEVEL': logging.INFO,
    'FEEDS': {
        filename: {
            "format": "json",
            "encoding": "utf8",
            "indent": 4
        },
    }
})

process.crawl(HotelsSpider)
process.start()