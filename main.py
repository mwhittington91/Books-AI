#https://developers.google.com/books/docs/v1/using#st_params

from enum import StrEnum, auto
import http
import json
import httpx
import os
import logging
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

def get_books(search_term, filter_type: SearchFilter|None = None, filter_term: str|None = None):
    """Get a list of books from Google Books API. Takes 
        in a search term, search filter and filter term.
        """
    reqUrl = f"https://www.googleapis.com/books/v1/volumes?q={search_term}+{filter_type}:{filter_term}&key={books_api_key}"

    response = httpx.get(reqUrl, headers={"Accept": "application/json"})

    output = response.json()['items']

    return json.dumps(output, indent=4, sort_keys=True)
    
webhook_url = os.getenv(key="ZAPIER_WEBHOOK_URL")
def add_to_book_list(book: str):
    """Adds a book to the user's book list. 
    Takes in a book object and returns the ISBN13 to the user"""

    # r= httpx.post(url="webhook_url",data={"isbn": isbn13})
    # return r.json()
    return book
