from dotenv import load_dotenv

load_dotenv()

from anthropic import Anthropic

client = Anthropic()

messages : list = []
MODEL_NAME="claude-haiku-4-5-20251001"
MAX_TOKEN = 200 

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
    
    


while True :
    user_input = input("> ")
    print(">", user_input)
    
    add_question(user_input)
    answer = chat_v2(messages, sys_prompt=system)
    
    print("-"*3)
    print(answer)
    print("-"*3)
    
    add_answer(answer)
    
    