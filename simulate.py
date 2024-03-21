'''
Use this script to run simulation job interviews from the command line.
Provide options to serve questions from predefined lists of technical and
behavioral questions.
Also include options to get questions and technical answers from ChatGPT using
its API.
'''
from numpy.random import choice
from random import shuffle
from sys import exit
from subprocess import run
from openai import OpenAI

with open('chatgpt_api_key.txt') as f:
    api_key = f.readline().strip('\n')

print('api key is', api_key)
print('\n')
client = OpenAI(api_key=api_key)
model = 'gpt-3.5-turbo'

def prompt_gpt(question, return_list=False):
    '''
    Thin wrapper around the OpenAI completions.create() function.
    Pass the prompt <question> to ChatGPT. 
    <return_list> (T/F) signifies whether or not the user requested multiple questions from ChatGPT.

    Return the single question or list of questions. 
    
    Note: The formatting of lists of questions from ChatGPT can be inconsistent, but the list prompts used here *usually* generate responses like the following:
    "['question 1?', \n'question 2?', \n'question 3', ...]"
    Replacing newlines with empty strings and reading in the entire string using eval() works when the response is in 
    this format and gives the desired list of questions.
    '''
    completion = client.chat.completions.create(model=model, messages=[{'role':'user', 'content':question}])
    response = completion.choices[0].message.content
    if return_list:
        try:
            response = eval(response.replace('\n', ''))
        except SyntaxError:
            print('\nError - Poor formatting from ChatGPT. Please try again. \n')
            response = None

    return response

def pop_q(qlist):
    '''
    Simple function to pop a question from the predefined list of questions <qlist>, or return None if all questions
    have already been popped and list is empty.
    '''
    try:
        q = qlist.pop()
    except IndexError:
        print('\nNo more questions of this type. Please try again or quit. \n')
        q = None

    return q

def serve_question(qtype):
    '''
    Generate a question. <qtype> will be fed in by the user. 
    Return the question or list of questions to be printed out.
    '''
    if qtype == 't':
        q = pop_q(technical_questions)
    elif qtype == 'b':
        q = pop_q(behavioral_questions)
    elif qtype == 'res':
        q = pop_q(resume_questions)
    elif qtype == 'q':
        pop_from = choice(['technical', 'behavioral', 'resume']) + '_questions'
        q = pop_q(eval(pop_from))
    elif qtype == 'gml':
        q = prompt_gpt('What are five common machine learning job interview questions? Return the questions in a python list with no additional text or formatting.', return_list=True)
    elif qtype == 'gstat':
        q = prompt_gpt('What are five common job interview questions about statistics and probability? Return the questions in a python list with no additional text or formatting.', return_list=True) 
    elif qtype == 'gcase':
        q = prompt_gpt('What are five common case study questions during data science job interviews? Return the questions in a python list with no additional text or formatting.', return_list=True)
    else:
        print('Exiting now. \n')
        exit()

    return q

with open('technical_questions.txt', 'r') as f:
    technical_questions = [line.replace('\n', '') for line in f]

with open('behavioral_questions.txt', 'r') as f:
    behavioral_questions = [line.replace('\n', '') for line in f]

with open('resume_questions.txt', 'r') as f:
    resume_questions = [line.replace('\n', '') for line in f]

qstr = 'What type of question would you like? \n' \
't -> technical question \n' \
'b -> behavioral question \n' \
'res -> question based on something from my resume \n'\
'q -> random choice between lists of technical, behavioral, and resume questions \n' \
'gml -> request five common ML interview questions from ChatGPT \n'\
'gstat -> request five common statistics and probability interview questions from ChatGPT \n'\
'gcase -> request five common DS interview case study questions from ChatGPT \n'\
'any other key -> exit the simulator \n'

nextprompt = 'What would you like to do next? \n' \
'a -> request a sample answer from ChatGPT \n' \
'q -> get another question \n' \
'any other key -> exit \n'

divstr = '\n' + '*' * 30 + '\n'

shuffle(technical_questions)
shuffle(behavioral_questions)
shuffle(resume_questions)
while True:
    qtype = input(qstr)
    q = serve_question(qtype)
    if q is None:
        # list of questions from ChatGPT was poorly formatted
        continue
    elif type(q) is list:
        # list of questions from ChatGPT was good
        for i, question in enumerate(q):
            run('clear')
            print(f'{i+1}. {question}')
            print(divstr)
            request_answer = input('Would you like to request a sample answer from ChatGPT? y/n \n')
            if request_answer == 'y':
                print('\n')
                print(prompt_gpt('Provide a sample answer to the following question: ' + question))
                _ = input('\nPress enter to continue. ')
    else:
        # must have requested a single question from predefined lists or ChatGPT
        run('clear')
        print(q)
        print(divstr)

        next_step = input(nextprompt)
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
