#https://developers.google.com/books/docs/v1/using#st_params

from enum import StrEnum, auto
import json
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

books_api_key: str | None = os.getenv(key='GOOGLE_BOOKS_API_KEY')

class SearchFilter(StrEnum):
    intitle = auto()
    inauthor = auto()
    isbn = auto()
    inpublisher = auto()
    subject = auto()
    lccn = auto()
    oclc = auto()

def get_books(search_term, filter_type: SearchFilter|None = None, filter_term: str|None = None, add_to_book_list: bool = False):
    """Get a list of books from Google Books API. Takes 
        in a search term, search filter and filter term.
        """
    webhook_url = os.getenv(key="ZAPIER_WEBHOOK_URL")

    reqUrl = f"https://www.googleapis.com/books/v1/volumes?q={search_term}+{filter_type}:{filter_term}&key={books_api_key}"

    response = httpx.get(reqUrl, headers={"Accept": "application/json"})

    output = response.json()['items']
    
    if add_to_book_list:
        """If the user request to add a book to their book list then this is True. Get the ISBN13 of the book and return it to the user."""
        identifiers = output[0]['volumeInfo']['industryIdentifiers']
        for identifier in identifiers:
            if identifier['type'] == 'ISBN_13':
                isbn_13 = identifier['identifier']
                httpx.post(webhook_url, json={"isbn_13": isbn_13})
                return f"Added {output[0]['volumeInfo']['title']} to your book list"
    else:
        return json.dumps(output, indent=4, sort_keys=True)
    


