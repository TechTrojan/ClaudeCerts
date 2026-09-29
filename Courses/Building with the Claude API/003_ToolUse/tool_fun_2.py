from datetime import datetime
from anthropic.types import ToolParam , Message
from BaseChat import  chat_tools

def add_user_message(messages, message):
    user_message = {
        "role": "user",
        "content": message.content if isinstance(message, Message) else message,
    }
    messages.append(user_message)


def add_assistant_message(messages, message):
    assistant_message = {
        "role": "assistant",
        "content": message.content if isinstance(message, Message) else message,
    }
    messages.append(assistant_message)

def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
    if not date_format:
        raise ValueError("date_format cannot be empty")
    return datetime.now().strftime(date_format)

def add_two_numbers(num1, num2):
    return num1+num2 


add_two_numbers_schema= ToolParam(
    {
  "name": "add_two_numbers",
  "description": "Add two numbers together and return their sum. Use this when the user asks to add, sum, or combine two numeric values, e.g. add_two_numbers(3, 5) returns 8, or add_two_numbers(2.5, 1.5) returns 4.0.",
  "input_schema": {
    "type": "object",
    "properties": {
      "num1": {
        "type": "number",
        "description": "The first addend, e.g. 3 or 2.5."
      },
      "num2": {
        "type": "number",
        "description": "The second addend, e.g. 5 or 1.5."
      }
    },
    "required": ["num1", "num2"]
  }
}
)

get_current_datetime_schema=  ToolParam(  {
  "name": "get_current_datetime",
  "description": "Get the current date and time, formatted according to a specified strftime-style format string. Returns the current local server time as a string (e.g. '2026-09-26 14:32:07' with the default format). Use this when the user asks for the current date, time, or timestamp.",
  "input_schema": {
    "type": "object",
    "properties": {
      "date_format": {
        "type": "string",
        "description": "A Python strftime-compatible format string controlling the output, e.g. '%Y-%m-%d %H:%M:%S' for '2026-09-26 14:32:07', '%B %d, %Y' for 'September 26, 2026', or '%H:%M' for '14:32'. Must be a non-empty string."
      }
    },
    "required": []
  }
}
)

def text_from_message(message):
    return "\n".join([block.text for block in message.content if block.type == "text"])


tools = [get_current_datetime_schema, add_two_numbers_schema]

import json


def tool_run_result(tool_use):
    tool_result= {
        "type":"tool_result",
        "tool_use_id" : tool_use.id
    }
    
    tool_params= tool_use.input
    
    if tool_use.name== 'get_current_datetime':
        result = get_current_datetime(**tool_params)
    elif tool_use.name == 'add_two_numbers':        
        result = add_two_numbers(**tool_params)

    tool_result["content"] = json.dumps(result) 
    tool_result["is_error"]= False 
    return tool_result  
    
def run_tools( msg )  :
    tool_requests = [ block for block in msg.content if block.type=='tool_use']
    # tool_requests=[]
    # for block in msg:
    #     if block["role"] == 'assistant' and block["content"].type == 'tool_use':
    #         tool_requests.append(block.content)
        
        
        
    tool_results=[]
    for tool_request in tool_requests:
        try:
            tool_result = tool_run_result(tool_request)

        except Exception as e:
            tool_result= {
                    "type":"tool_result",
                    "tool_use_id" : tool_request.id,
                    "content": f"Error {e}",
                    "is_error": True 
                }

        tool_results.append(tool_result)

    return tool_results
        
        
 

# messages.append(
#     {
#         'role' : 'assistant',
#         'content' : response.content
#     }
# )

def run_conversation(messages):
    while True:
        response = chat_tools(messages, tools)

        add_assistant_message(messages, response)
        print(text_from_message(response))
        
        if response.stop_reason!='tool_use':
            break

        print(response)    

        tool_results = run_tools(response)
        add_user_message(messages, tool_results)

    return messages        
        
            
        
        
        


messages=[]
messages.append(
    {
        'role' : 'user',
        'content' : 'What is the exact time, formatted as HH:MM:SS ? and add two numbers  3 and 8. ' 
    }
)
    
    
messages = run_conversation(messages)         
print(messages)
        
             
         