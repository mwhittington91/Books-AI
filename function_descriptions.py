function_descriptions = [{
    "type": "function",
    "function":
    {
        "name": "get_books",
        "description": """Get a list of books from Google Books API. Takes 
        in a search term, search filter and filter term. Here is an example of searching
        for a list of books with 'Mist' in the title and an authour with the name 'Brandon':
        get_books(search_term=Mist,filter_type=inauthor,filter_term=Brandon)
        """,
        "parameters": {
            "type": "object",
            "properties": {
                "search_term": {
                    "type": "string",
                    "description": "The search term to use for the Google Books API",
                },
                "filter_type": {
                    "type": "string",
                    "description": """The type of filter to be used with the filter term.
                        There must be a filter to go with the filter type.
                        Only use the options listed in the enum""",
                    "enum": ["intitle", "inauthor", "isbn", "inpublisher", "subject", "lccn", "oclc"],
                },
                "filter_term": {
                    "type": "string",
                    "description": """The filter term to use with the filter type.
                        There must be a filter type to go with the filter term.
                        For example, if the filter type is 'inauthor', 
                        the filter term could be the author's name, like 'Brandon Sanderson"""
                    ,
                },
            },
            "required": ["search_term"],
        },
    }
    },
    {
        "type": "function",
        "function":
        {
            "name": "add_to_book_list",
            "description": """Adds a book to the user's book list. 
            Takes in a book's ISBN13 and adds it to the user's book list""",
            "parameters": {
                "type": "object",
                "properties": {
                    "isbn13": {
                        "type": "string",
                        "description": "The ISBN13 to send to the user",
                    },
                },
                "required": ["isbn13"],
            },
        }
    }
    
   
]