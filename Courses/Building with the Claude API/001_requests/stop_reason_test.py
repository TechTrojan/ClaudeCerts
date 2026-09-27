from dotenv import load_dotenv

load_dotenv()

from anthropic import Anthropic

client = Anthropic()

messages : list = []
MODEL_NAME="claude-haiku-4-5-20251001"
MAX_TOKEN = 100 

def chat(messages, sys_prompt:str  ):
    
    response = client.messages.create(
        model = MODEL_NAME,
        max_tokens= MAX_TOKEN, 
        messages= messages,
        system= sys_prompt
        
    )
    
    return response.content[0].text 



def chat_v2(messages, sys_prompt:None ):
    
    params = {
        'model' : MODEL_NAME,
        'max_tokens' : MAX_TOKEN, 
        'messages' : messages
    }
    
    if sys_prompt:
        params['system'] = sys_prompt
        
    response = client.messages.create(        
       **params        
    )
    
    return response.content[0].text 


def chat_v3(messages, sys_prompt:None ):
    
    params = {
        'model' : MODEL_NAME,
        'max_tokens' : MAX_TOKEN, 
        'messages' : messages
    }
    
    if sys_prompt:
        params['system'] = sys_prompt
        
    response = client.messages.create(        
       **params        
    )
    
    return response

def add_question(question):
    q = {
        'role' : 'user',
        'content' : question
    }
    messages.append(q)
    
def add_answer(answer)  :
    messages.append(
        {
            'role':'assistant',
            'content': answer
            
        }
    )

system= """
You are a patient math tutor.
Do not directly answer a student's question.
Guide them to a solution step by step.
"""
    
    

user_input = "[Unsafe request]"
print(">", user_input)

add_question(user_input)
response  = chat_v3(messages, sys_prompt=None )

#print("-"*3)
print(response)

if response.stop_reason == 'end_turn':
    for block in response.content:
        if block.type == 'text':
            print(block.text) 
elif response.stop_reason == 'max_tokens'  :
    print(response.content[0].text)
    print("response was cut off at token limit")
elif response.stop_reason == 'refusal'    :
    print("Claude was unable to process this request")
            
    
    