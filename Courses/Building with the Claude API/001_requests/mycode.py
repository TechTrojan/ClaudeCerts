from dotenv import load_dotenv 


load_dotenv()


from anthropic import Anthropic

client = Anthropic()
model= "claude-sonnet-4-0"
MODEL_NAME="claude-haiku-4-5-20251001"
#MODEL_NAME="claude-sonnet-5"


messages:list = []


def add_user_message(messages:list , question:str):
    single_message = {
        'role': 'user',
        'content': question
    }
    
    messages.append(single_message)


def add_AI_message(messages:list , question:str):
    single_message = {
        'role': 'assistant',
        'content': question
    }
    
    messages.append(single_message)    
    

def chat(messages:list) :

    response  = client.messages.create(
        model=MODEL_NAME, 
        max_tokens= 500, 
        messages=messages
        
    )

    return response.content[0].text

    

add_user_message(messages, "Explain quantum computing. ")    

answer = chat(messages)

print(answer)

print("-"*50)


add_AI_message(messages, answer)

print(messages)

print("-"*50)

add_user_message(messages, "Write one sentence about it.")

answer2= chat(messages)

add_AI_message(messages, answer2)

print("-"*50)

print('all messages')

print(messages)










