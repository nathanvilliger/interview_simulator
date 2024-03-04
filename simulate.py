'''
Use this script to run simulation job interviews from the command line.
Provide options to serve questions from predefined lists of technical and
behavioral questions.
Also include options to get questions and technical answers from ChatGPT using
its API.
'''
from numpy.random import uniform, choice
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

technical_questions = [
    'What is a p value?',
    'Why do ML models overfit? How can it be prevented?',
    'What was your PhD research about?',
    'Tell me about a time you used analytics in a previous project.',
    'What are the assumptions required for a linear regression?',
    'How do you handle a dataset missing several values?',
    'How do you explain technical aspects of your results to stakeholders with '\
    'a non-technical background?',
    'What are the feature selection methods used to select the right variables for '\
    'a machine learning model?',
    'List the different types of relationships between tables in SQL.',
    'What is dimensionality reduction? Why would you do it?',
    'What is the goal of A/B Testing?',
    'Explain confidence intervals',
    'How do you manage an unbalanced dataset when training ML models?',
    'How do you evaluate the performance of a clustering model, where there are '\
    'no known labels?',
    'There are four people in an elevator and four floors in a building. What is '\
    'the probability that each person gets off on a different floor?'
]

behavioral_questions = [
    'What is your biggest strength?',
    'What is your biggest weakness?',
    'Tell me about a time when you had to explain a complex data concept ' \
    'to someone without a technical background. How did you ensure they understood?',
    'Describe a project where you had to work with a difficult team member. '\
    'How did you handle the situation?',
    'Can you share an example of a time when you had to work under a tight deadline? '\
    'How did you manage your tasks and deliver on time?',
    'Have you ever made a significant mistake in your analysis? How did you handle it '\
    'and what did you learn from it?',
    'How do you stay updated with the latest trends and advancements in data science?',
    'Can you tell us about a time when you had to work on a project with unclear or '\
    'constantly changing requirements? How did you adapt?',
    'Tell me about a time when you worked as part of a team to successfully execute a project.',
    'What is a project that you are most proud of?',
    'Tell me about a time you failed.',
    'Tell me about a time when you demonstrated leadership.',
    'Have you ever had to make an unpopular decision? How did you handle it?',
    'Describe a time when you were under a lot of pressure at work. How did you react?',
    'Tell me about a mistake you have made. How did you handle it?',
    'Explain a situation where you used data or logic to make a recommendation.',
    'Describe a time when you had to deliver bad news. How did you do it?',
    'Share an example of a time when you failed. What did you learn from the experience?',
    'Tell me about the last time your workday ended before you were able to get everything done.'
]

# these will be specific to my resume -- change them to interrogate bullet points from yours
resume_questions = [
    'Describe your experience with programming languages like Python and R.',
    'Do you have experience working in a unix environment or bash scripting?',
    'Describe your experience with SQL. How have you used it?',
    'Describe your experience with Big Data tools like Databricks and PySpark.',
    'How did you use exploratory data analysis and data visualization in your research?',
    'What statistical tests have you used and why?',
    'Tell me about your experience with machine learning.',
    'How many years of experience do you have building data dashboards?',
    'Have you collaborated on software projects with Git?',
    'What is a neural network?',
    'What is a convolutional neural network? Why did you use that type of model in your "Estimating Dispersal..." project?',
    'What is multidimensional scaling? Why did you use it in your "Estimating Dispersal..." project?',
    'How and why did you establish the collaboration with the bio group? What did either side have to gain?',
    'What "relevant summary statistics" did you include in the simulations you designed? Why?',
    'What did your simulation pipeline entail?',
    'What did your data mining and analysis routines look like?',
    'What statistical tests and procedures did you use to discover information in large datasets?',
    'How did you go about learning new research tools and techniques?',
    'What challenges did you face in sharing results and methods with colleagues?',
    'What was novel about the measurement techniques you used in your explicit local dynamics project?',
    'How did you capture breakdowns of simplified models of expanding populations?'
]

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
                _ = input('\nPress any key to continue. ')
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
