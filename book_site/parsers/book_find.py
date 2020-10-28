from pprint import pprint

import bs4
from urllib import request

from book_site.parsers.utils import get_html


def labirint_search(book):
    html = get_html(f'https://www.labirint.ru/search/{book}/?order=relevance&way=back&stype=0&available=1&price_min'
                    f'=&price_max=')
    soup = bs4.BeautifulSoup(html, 'html.parser')
    labirint_find = soup.find('div', class_='products-row')
    titles = [title.text.strip('\n') for title in list(labirint_find.find_all('a', class_='product-title-link'))]
    author = ''
    return titles

print(labirint_search('томминокеры'))
