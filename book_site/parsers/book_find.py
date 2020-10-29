import json
from collections import OrderedDict
from pprint import pprint

import bs4
from urllib import request

from book_site.parsers.utils import get_html


def labirint_search(book):
    html = get_html(f'https://www.labirint.ru/search/{book}/?order=relevance&way=back&stype=0&available=1&price_min'
                    f'=&price_max=')
    soup = bs4.BeautifulSoup(html, 'html.parser')
    labirint_find = soup.find('div', class_='products-row')
    result = OrderedDict({'title': [title.text.replace('\n', '') for title in
                                    list(labirint_find.find_all('a', class_='product-title-link'))],
                          'author': [author.text.replace('\n', '').rstrip() for author in
                                     list(labirint_find.find_all('div', class_='product-author'))],
                          'pubhouse': [pubhouse.text.replace('\n', '') for pubhouse in
                                       list(labirint_find.find_all('div', class_='product-pubhouse'))],
                          'covers': [image['data-src'] for image in labirint_find.find_all('img')],
                          'labirint_price': [price.text.strip('₽\r\n\t\t').rstrip() for price in
                                             list(labirint_find.find_all('span', class_='price-val'))],
                          'labirint_link': [f"https://www.labirint.ru{link['href']}" for link in
                                            labirint_find.find_all('a', class_='cover')]})

    return result
