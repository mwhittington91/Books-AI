import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

books_api_key: str | None = os.getenv('GOOGLE_BOOKS_API_KEY')

def get_books(search_term, search_type=None):
    reqUrl = f"https://www.googleapis.com/books/v1/volumes?q={search_term}+{search_type}&key={books_api_key}"

    headersList = {
     "Accept": "*/*" 
    }

    response = requests.request("GET", reqUrl, headers=headersList)

    output = response.json()['items']

    return json.dumps(output, indent=4, sort_keys=True)

