
from BaseChat import add_assistant_message, add_user_message, chat
from CodeGrader import grade_syntax 

def run_prompt(test_case):
    """Merges the prompt and test case input, then return the result"""
    prompt=f"""
    Please solve the following task:
    
    {test_case['task']}
    
    * Respond only with Python, JSON or a plain Regex
    * do not add any comments or commentary or explaination 
    
    """
    
    messages=[]
    add_user_message(messages, prompt)
    add_assistant_message(messages, "```code")
    text = chat(messages, stop_sequences=["```"])
    return text 

def grade_by_model(test_case,output):
    """Evaluate test case prompt and answer. Provide result a score with strength, weakness and reasoning.

    Args:
        testcase (dict): Test case that needs to grade
        output (string): 
    """
    
    eval_prompt = f"""
You are an expert AWS code reviewer. Your task is to evaluate the following AI-generated solution.

Original Task:
<task>
{test_case["task"]}
</task>

Solution to Evaluate:
<solution>
{output}
</solution>

Output Format
Provide your evaluation as a structured JSON object with the following fields, in this specific order:
- "strengths": An array of 1-3 key strengths
- "weaknesses": An array of 1-3 key areas for improvement
- "reasoning": A concise explanation of your overall assessment
- "score": A number between 1-10

Respond with JSON. Keep your response concise and direct.
Example response shape:
{{
    "strengths": string[],
    "weaknesses": string[],
    "reasoning": string,
    "score": number
}}
    """

    messages = []
    add_user_message(messages, eval_prompt)
    add_assistant_message(messages, "```json")
    eval_text = chat(messages, stop_sequences=["```"])
    return json.loads(eval_text)
    

def run_test_case(test_case):
    """ Executes the test case and returns task, output and score of result.

    Args:
        test_case (dict): Test case that needs to execute
    """
    
    output = run_prompt(test_case)
    
    grade_result = grade_by_model(test_case, output)
    code_grader = grade_syntax(output, test_case )
    
    score =( int(grade_result['score']) + code_grader ) /2
    
    
    
    result = {
        'task' : test_case['task'],
        'output' : output,
        'reasoning': grade_result['reasoning'] ,
        'strengths': grade_result['strengths'] ,
        'weaknesses': grade_result['weaknesses'] ,
        'syntax_score ' :  code_grader, 
        'model_score': grade_result['score'] ,
        'score' : score 
        
    }
    
    return result 


def run_eval(dataset:list):
    """Loads the dataset and calls 'run_test_case' with each case 

    Args:
        dataset (list): dataset that has list of tasks to evaluate
    """
    
    results=[]
    
    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)
        
    return results



import json 

with open("dataset.json","r")  as f:
    dataset = json.load(f)



eval_result = run_eval(dataset)

print(json.dumps(eval_result, indent=2))


with open("eval_result_2.json", "w") as f:
    json.dump(eval_result, f, indent=2) 

    