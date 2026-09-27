
from dotenv import load_dotenv 
from anthropic import Anthropic

load_dotenv()

client = Anthropic()
MODEL_NAME ="claude-haiku-4-5-20251001"
#MODEL_NAME="claude-sonnet-5"
MAX_TOKEN = 1000



def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)




def chat(messages, system=None, temperature=1.0, stop_sequences=[], tools = None ):
    params = {
        "model": MODEL_NAME,
        "max_tokens": MAX_TOKEN,
        "messages": messages,
        #"temperature": temperature,
        "stop_sequences": stop_sequences,
    }

    if system:
        params["system"] = system
    
    if tools:
        params['tools'] = tools 

    message = client.messages.create(**params)
    return message.content[0].text


def chat_tools(messages:list, tools = None ) :

    response  = client.messages.create(
        model=MODEL_NAME, 
        max_tokens= 500, 
        messages=messages,
        tools= tools 
        
    )

    return response
