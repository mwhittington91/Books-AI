import logging
import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from main import get_books
from function_descriptions import function_descriptions
load_dotenv()

import colorlog

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s:%(name)s:%(message)s'))

logger = colorlog.getLogger()
logger.addHandler(handler)
logger.setLevel(level=logging.INFO)

api_key: str | None = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

def run_conversation(question:str):
    # Step 1: send the conversation and available functions to the model
    messages = [{"role": "system", "content": """You are a helpful, digtal libriarian.  
                 You help users search for books based on certian criteria and can add books to their book lists.
                 You can a set of functions to help you do this. You can user multiple functions in a single request."""},
        {"role": "user", "content": question}]
    tools = function_descriptions
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
        tools=tools,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    logger.info(msg=response_message)
    # Step 2: check if the model wanted to call a function
    if tool_calls:
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = [{
            "get_books": get_books}] 
        messages.append(response_message)  # extend conversation with assistant's reply
        # Step 4: send the info for each function call and function response to the model
        for tool_call in tool_calls:
            function_name: str = tool_call.function.name
            function_to_call = [func for func in available_functions if function_name in func][0][function_name]
            function_args = json.loads(s=tool_call.function.arguments)
            logger.info(msg=function_args)
            function_response: str = function_to_call(**(dict(function_args))
            )
            logger.info(msg=function_response)
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )  # extend conversation with function response
        second_response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages,
        )  # get a new response from the model where it can see the function response
        return second_response.choices[0].message.content
    
if __name__ == "__main__":
    print(run_conversation(question='Search for "Magic for Liars" by "Sarah Gailey" and add it to my book list.'))
