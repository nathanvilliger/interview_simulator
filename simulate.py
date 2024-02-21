'''
Use this script to run simulation job interviews from the command line.
Provide options to serve questions from predefined lists of technical and
behavioral questions.
Also include options to get questions and technical answers from ChatGPT using
its API.
'''
from numpy.random import uniform, choice
from sys import exit
from openai import OpenAI

with open('chatgpt_api_key.txt') as f:
    api_key = f.readline().strip('\n')

print('api key is', api_key)
print('\n' * 3)
client = OpenAI(api_key=api_key)
model = 'gpt-3.5-turbo'

def prompt_gpt(question):
    '''
    Thin wrapper around the OpenAI completions.create() function.
    Pass the prompt <question>.
    Return the text of the response.
    '''
    completion = client.chat.completions.create(model=model, messages=[{'role':'user', 'content':question}])
    response = completion.choices[0].message.content
    return response

def serve_question(qtype):
    '''
    Generate a question. <qtype> will be fed in by the user.
    Return the question to be printed out.
    '''
    if qtype == 't':
        q = choice(technical_questions)
    elif qtype == 'b':
        q = choice(behavioral_questions)
    elif qtype == 'q':
        if uniform() < 0.5:
            q = choice(technical_questions)
        else:
            q = choice(behavioral_questions)
    elif qtype == 'gt':
        q = prompt_gpt('What is a common technical question during data science job interviews? Give me just the question and no extra text.')
    elif qtype == 'gb':
        q = prompt_gpt('What is a common behavioral question during job interviews? Give me just the question and no extra text.')
    else:
        print('Not a valid choice. \nExiting now. \n')
        exit()

    return q

technical_questions = [
    'What is a p value?',
    'Why do ML models overfit? How can it be prevented?'
]

behavioral_questions = [
    'What is your biggest strength?',
    'What is your biggest weakness?'
]

qstr = 'What type of question would you like? \n' \
't -> technical question \n' \
'b -> behavioral question \n' \
'q -> random choice between list of technical and behavioral questions \n' \
'gt -> request a common DS interview question from ChatGPT \n'\
'gb -> request a common behavioral question from ChatGPT \n'

nextprompt = 'What would you like to do next? \n' \
'a -> request a sample answer from ChatGPT \n' \
'q -> get another question \n' \
'any other key -> exit \n'

divstr = '\n' * 3 + '*' * 30 + '\n' * 3

while True:
    qtype = input(qstr)
    print('\n' * 3)
    q = serve_question(qtype)
    print(q)
    print(divstr)

    next_step = input(nextprompt)
    print('\n')
    if next_step == 'a':
        print(divstr)
        print(prompt_gpt('Provide a sample answer to the following question: ' + q))
        print(divstr)
        new_next = input('Would you like another question? y/n \n')
        if new_next != 'y':
            print('Goodbye and good luck.')
            exit()
    elif next_step != 'q':
        print('Goodbye and good luck.')
        exit()
    else:
        print(divstr)
