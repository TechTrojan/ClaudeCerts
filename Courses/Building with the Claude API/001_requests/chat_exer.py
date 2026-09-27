from dotenv import load_dotenv

load_dotenv()

from anthropic import Anthropic

client = Anthropic()

messages : list = []
MODEL_NAME="claude-haiku-4-5-20251001"
MAX_TOKEN = 200 

def chat(messages ):
    
    response = client.messages.create(
        model = MODEL_NAME,
        max_tokens= MAX_TOKEN, 
        messages= messages
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
    
    


while True :
    user_input = input("> ")
    print(">", user_input)
    
    add_question(user_input)
    answer = chat(messages)
    
    print("-"*3)
    print(answer)
    print("-"*3)
    
    add_answer(answer)
    
    