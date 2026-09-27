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
        system= sys_prompt,
        stream=True 
        
    )
    
    return response 



def chat_stream(messages, sys_prompt:None ) :
    
    params = {
        'model' : MODEL_NAME,
        'max_tokens' : MAX_TOKEN, 
        'messages' : messages,
        'stream' : True 
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
    
    



# user_input = input("> ")
# print(">", user_input)

#Method 1 
# add_question("Write a 1 sentence description of a fake LLM")
# stream  = chat_stream(messages, sys_prompt=None )

# for event in stream:
#     print(event)

add_question("Write a 1 sentence description of a fake operating system.")

with client.messages.stream(
    model=MODEL_NAME,
    max_tokens=300   ,
    messages=messages
)    as stream:
    
    for text in stream.text_stream:
        print(text, end="")
        
     
    