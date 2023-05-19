import json
import timeit
from datetime import datetime
from models import Author
from models import Quote


def load_authors():
    with open('authors.json') as file:
        authors_data = json.load(file)

    for author_data in authors_data:
        fullname = author_data['fullname']
        existing_author = Author.objects(fullname=fullname).first()

        if not existing_author:
            born_date_str = author_data['born_date']
            born_date = datetime.strptime(born_date_str, "%B %d, %Y")
            author = Author(
                fullname=fullname,
                born_date=born_date,
                born_location=author_data['born_location'],
                description=author_data['description']
            )
            author.save()


def load_quotes():
    with open('quotes.json') as file:
        quotes_data = json.load(file)

        for quote_data in quotes_data:
            author_name = quote_data['author']
            quote_text = quote_data['quote']
            author = Author.objects(fullname=author_name).first()
            existing_quote = Quote.objects(author=author,
                                           quote=quote_text).first()

            if not existing_quote:
                if author:
                    quote = Quote(
                        tags=quote_data['tags'],
                        author=author,
                        quote=quote_text
                    )
                    quote.save()


if __name__ == '__main__':
    start = timeit.default_timer()
    load_authors()
    print(f"Result time: {timeit.default_timer() - start}")

    start = timeit.default_timer()
    load_quotes()
    print(f"Result time: {timeit.default_timer() - start}")
