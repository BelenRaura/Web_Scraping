import scrapy


class ExampleSpiderSpider(scrapy.Spider):
    name = "example_spider"
    allowed_domains = ["aminoapps.com"]
    start_urls = ["https://aminoapps.com/c/k-pop-es/home/"]

    def parse(self, response):
        # Extraer títulos de publicaciones o secciones
        for post in response.css('h2::text'):
            yield {
                'title': post.get()
            }

        # Extraer enlaces a otras páginas
        for link in response.css('a::attr(href)'):
            yield {
                'link': response.urljoin(link.get())
            }

        # Opción de seguir paginación (si existe)
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
