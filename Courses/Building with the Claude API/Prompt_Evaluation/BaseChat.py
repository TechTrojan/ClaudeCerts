
from dotenv import load_dotenv 
from anthropic import Anthropic

load_dotenv()

client = Anthropic()
MODEL_NAME ="claude-haiku-4-5-20251001"
MAX_TOKEN = 1000



def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)



def chat(messages, system=None, temperature=1.0, stop_sequences=[]):
    params = {
        "model": MODEL_NAME,
        "max_tokens": MAX_TOKEN,
        "messages": messages,
        #"temperature": temperature,
        "stop_sequences": stop_sequences,
    }

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message.content[0].text
