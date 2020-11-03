from pprint import pprint

import bs4

from book_site.parsers.utils import get_html


def labirint_search(book):
    html = get_html(f'https://www.labirint.ru/search/{book}/?order=relevance&way=back&stype=0&available=1&price_min'
                    f'=&price_max=')
    soup = bs4.BeautifulSoup(html, 'html.parser')
    labirint_find = soup.find('div', class_='products-row')
    try:
        result = {
            'labirint_id': [labirint_id['data-product-id'] for labirint_id in
                            list(labirint_find.find_all('div', class_='product need-watch'))],
            'title': [title.text.replace('\n', '') for title in
                      list(labirint_find.find_all('a', class_='product-title-link'))],
            'author': [author['alt'].split('-')[0].replace('обложка книги', '').rstrip() for author
                       in labirint_find.find_all('img', class_='book-img-cover')],
            'pubhouse': [pubhouse.text.replace('\n', '') for pubhouse in
                         list(labirint_find.find_all('div', class_='product-pubhouse'))],
            'covers': [image['data-src'] for image in labirint_find.find_all('img')],
            'labirint_price': [price.text.strip('₽\r\n\t\t').rstrip() for price in
                               list(labirint_find.find_all('span', class_='price-val'))],
            'labirint_link': [f"https://www.labirint.ru{link['href']}" for link in
                              labirint_find.find_all('a', class_='cover')]}
    except AttributeError:
        result = []
        return result

    return result


def labirint_result(result):
    result_dict = {}
    try:
        result_length = len(result['title'])
        for i in range(result_length):
            result_dict[i] = {'labirint_id': result['labirint_id'][i],
                              'title': result['title'][i],
                              'author': result['author'][i],
                              'pubhouse': result['pubhouse'][i],
                              'cover': result['covers'][i],
                              'labirint_price': result['labirint_price'][i],
                              'labirint_link': result['labirint_link'][i]}
    except TypeError:
        result_dict = {}

    return result_dict


def book24_search(book):
    html = get_html(f'https://book24.ru/search/?q={book}&available=1')
    soup = bs4.BeautifulSoup(html, 'html.parser')
    book24_find = soup.find('div', class_='catalog-products__list js-catalog-products')
    return book24_find