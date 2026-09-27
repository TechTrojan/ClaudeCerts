from datetime import datetime
from anthropic.types import ToolParam 
from BaseChat import add_user_message, add_assistant_message, chat_tools


def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
    if not date_format:
        raise ValueError("date_format cannot be empty")
    return datetime.now().strftime(date_format)


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


messages=[]
messages.append(
    {
        'role' : 'user',
        'content' : 'What is the exact time, formatted as HH:MM:SS ? ' 
    }
)


tools = [get_current_datetime_schema]

response = chat_tools(messages, tools= tools )

messages.append(
    {
        'role' : 'assistant',
        'content' : response.content
    }
)

print (messages)

print("*"*20)

#print(**response.content[0].input )

tool_input = response.content[0].input


result = get_current_datetime(**tool_input )


messages.append(
    {
        "role"  : "user",
        "content" : [
            {
            'type' : 'tool_result',
            'tool_use_id' : response.content[0].id ,
            'content' : result , 
            'is_error' : False 
            }
        ]
    }
)

response_2 = chat_tools(messages, tools= tools )
print(response_2 )
