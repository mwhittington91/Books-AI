import os
import json
import openai
from datetime import datetime, timedelta
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, ChatMessage
from main import get_books

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

function_descriptions = [
    {
        "name": "get_books",
        "description": "Get a list of books from Google Books API",
        "parameters": {
            "type": "object",
            "properties": {
                "search_term": {
                    "type": "string",
                    "description": "The search term to use for the Google Books API",
                },
                "search_type": {
                    "type": "string",
                    "description": "The type of search to perform. Only use the options listed in the enum",
                    "enum": ["intitle", "inauthor", "isbn", "inpublisher", "subject", "lccn", "oclc"],
                },
            },
            "required": ["search_term"],
        },
    }
]

llm = ChatOpenAI(model="gpt-3.5-turbo-16k", temperature=0)

# Start a conversation with multiple requests

user_prompt = "Get me a list of books published by Tor Books with an author named Brandon Sanderson"

first_response = llm.predict_messages(
    [HumanMessage(content=user_prompt)], functions=function_descriptions
)

print(first_response)
args = json.loads(first_response.additional_kwargs.get('function_call')['arguments'])
# print(args)
# print(type(args))

# print(get_books(**args))

second_response = llm.predict_messages(
    [
        HumanMessage(content=user_prompt),
        AIMessage(content=str(first_response.additional_kwargs)),
        AIMessage(
            role="function",
            additional_kwargs={
                "name": first_response.additional_kwargs["function_call"]["name"]
            },
            content=f"Completed function {first_response.additional_kwargs['function_call']['name']} with arguments {first_response.additional_kwargs['function_call']['arguments']}",
        ),
    ],
    functions=function_descriptions,
)

print(second_response)