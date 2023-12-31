book_example = {
        "accessInfo": {
            "accessViewStatus": "NONE",
            "country": "US",
            "embeddable": "false",
            "epub": {
                "isAvailable": "false"
            },
            "pdf": {
                "isAvailable": "false"
            },
            "publicDomain": "false",
            "quoteSharingAllowed": "false",
            "textToSpeechPermission": "ALLOWED",
            "viewability": "NO_PAGES",
            "webReaderLink": "http://play.google.com/books/reader?id=0b-vzgEACAAJ&hl=&source=gbs_api"
        },
        "etag": "001DtGPlik4",
        "id": "0b-vzgEACAAJ",
        "kind": "books#volume",
        "saleInfo": {
            "country": "US",
            "isEbook": "false",
            "saleability": "NOT_FOR_SALE"
        },
        "searchInfo": {
            "textSnippet": "Who can Joey save? Who wants to be saved? And can she even survive to tell the tale?"
        },
        "selfLink": "https://www.googleapis.com/books/v1/volumes/0b-vzgEACAAJ",
        "volumeInfo": {
            "allowAnonLogging": "false",
            "authors": [
                "Sarah Gailey"
            ],
            "canonicalVolumeLink": "https://books.google.com/books/about/Eat_the_Rich_SC.html?hl=&id=0b-vzgEACAAJ",
            "categories": [
                "Comics & Graphic Novels"
            ],
            "comicsContent": "true",
            "contentVersion": "preview-1.0.0",
            "description": "When the rich and powerful are literal cannibals, how can regular people avoid being on the menu? WELCOME TO CRESTFALL BLUFFS! With law school and her whole life ahead of her, Joey plans to spend the summer with her boyfriend Astor at his seemingly perfect family home. But beneath all the affluent perfection lies a dark, deadly rot\u2026 something all the locals live in quiet fear of. As summer lingers, Joey uncovers the macabre history of Crestfall Bluffs, and the ruthlessness and secrecy lying in wait behind the idyllic lives of the one percent. Who can Joey save? Who wants to be saved? And can she even survive to tell the tale? The bold, horrifying psychological thriller from Hugo Award-winning author Sarah Gailey (The Echo Wife, Magic For Liars) and artist Pius Bak (Firefly, The Magicians) with colorist Roman Titov and letterer Cardinal Rae. Collects Eat the Rich #1-5.",
            "imageLinks": {
                "smallThumbnail": "http://books.google.com/books/content?id=0b-vzgEACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
                "thumbnail": "http://books.google.com/books/content?id=0b-vzgEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
            },
            "industryIdentifiers": [
                {
                    "identifier": "168415832X",
                    "type": "ISBN_10"
                },
                {
                    "identifier": "9781684158324",
                    "type": "ISBN_13"
                }
            ],
            "infoLink": "http://books.google.com/books?id=0b-vzgEACAAJ&dq=Magic+for+Liars+inauthor:Sarah+Gailey&hl=&source=gbs_api",
            "language": "en",
            "maturityRating": "NOT_MATURE",
            "pageCount": 128,
            "panelizationSummary": {
                "containsEpubBubbles": "false",
                "containsImageBubbles": "false"
            },
            "previewLink": "http://books.google.com/books?id=0b-vzgEACAAJ&dq=Magic+for+Liars+inauthor:Sarah+Gailey&hl=&cd=10&source=gbs_api",
            "printType": "BOOK",
            "publishedDate": "2022-05-24",
            "publisher": "BOOM! Studios",
            "readingModes": {
                "image": "false",
                "text": "false"
            },
            "title": "Eat the Rich SC"
        }
    }

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
                "add_to_book_list": {
                    "type": "boolean",
                    "description": """If the user request to add a book to their book list then this is True.
                    The default is False""",
                },
            },
            "required": ["search_term"],
        },
    }
    },
    # {
    #     "type": "function",
    #     "function":
    #     {
    #         "name": "add_to_book_list",
    #         "description": """Use this when a user asks to add a book to their book list.""",
    #         "parameters": {
    #             "type": "object",
    #             "properties": {
    #                 "book": {
    #                     "type": "object",
    #                     "description": f"json object of the book to be added to the user's book list. Here is an example of a book object: {book_example}",
    #                 },
    #             },
    #             "required": ["book"],
    #         },
    #     }
    # }
]

