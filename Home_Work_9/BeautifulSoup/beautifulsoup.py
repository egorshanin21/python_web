import requests
import json
from bs4 import BeautifulSoup
import re


def extract_quotes_data(soup):
    quotes = []
    quote_divs = soup.find_all('div', class_='quote')

    for quote_div in quote_divs:
        quote = quote_div.find('span', class_='text').text
        author = quote_div.find('small', class_='author').text
        tags = [tag.text for tag in quote_div.find_all('a', class_='tag')]

        quote_data = {
            'tags': tags,
            'author': author,
            'quote': quote
        }
        quotes.append(quote_data)

    return quotes


def extract_authors_data(soup):
    authors = []
    author_links = soup.select('.author + a[href*="/author/"]')
    added_authors = set()

    for author_link in author_links:
        author_url = author_link['href']
        author_page = requests.get(f'http://quotes.toscrape.com{author_url}')
        author_soup = BeautifulSoup(author_page.content, 'html.parser')

        name = author_soup.find('h3', class_='author-title')
        author_name = re.match(r'^([^:]+)', name.get_text(strip=True)).group(1)
        author_name = author_name[:-4] if len(
            author_name) > 4 else author_name if name else ' '

        if author_name not in added_authors:
            born_date_element = author_soup.find('span', class_='author-born-date')
            born_date = born_date_element.text.strip() if born_date_element else ''

            born_location_element = author_soup.find('span', class_='author-born-location')
            born_location = born_location_element.text.strip() if born_location_element else ''

            description_element = author_soup.find('div', class_='author-description')
            description = description_element.text.strip() if description_element else ''

            author_data = {
                'fullname': author_name,
                'born_date': born_date,
                'born_location': born_location,
                'description': description
            }
            authors.append(author_data)
            added_authors.add(author_name)

    return authors


def scrape_quotes():
    all_quotes = []
    authors_data = []

    for page in range(1, 11):
        url = f"http://quotes.toscrape.com/page/{page}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        quotes = extract_quotes_data(soup)
        authors_data.extend(extract_authors_data(soup))
        all_quotes.extend(quotes)

    save_quotes_to_json(all_quotes)
    save_authors_to_json(authors_data)


def save_authors_to_json(data):
    with open('authors.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def save_quotes_to_json(data):
    with open('quotes.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


scrape_quotes()
