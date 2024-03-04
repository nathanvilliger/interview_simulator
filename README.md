# Job interview simulator

Use `simulate.py` to simulate data science job interviews from the command line.
The script serves up behavioral, technical, and resume questions from predefined lists
as requested by the user. It also includes the option to ask ChatGPT for sample
questions and answers! ChatGPT functionality requires a little setup; see below for details.

Good luck!

## Usage

Simply run `python simulate.py` from the command line to enter the simulator. The application provides for two basic use patterns:

- Single questions at a time, either drawn from the predefined lists of questions or provided by ChatGPT. I recommend drawing from the predefined lists for this use case since ChatGPT may repeat itself when given the same question prompt over and over.  

- Several questions in a row provided in one go by ChatGPT. The code is currently written to ask for a list of five questions at a time in this mode, but that number could easily be changed by changing the prompts in the calls to `prompt_gpt()` within the `serve_question()` function (specifically the calls where `return_list=True`).

Note that the resume questions interrogate bullet points from my resume. You'll want to change those to make them relevant to you!

## ChatGPT setup

There's some quick setup that needs to be done before you can run the simulator and take advantage of the ChatGPT functionality. These steps are meant to be minimal and easy to follow; check out the [ChatGPT API documentation](https://platform.openai.com/docs/quickstart?context=python) for more information if you're interested.

1. Create an OpenAI account or sign in if you have one already.

1. Navigate to the [API key page](https://platform.openai.com/account/api-keys) and "Create new secret key."

1. Store the key in a file called `chatgpt_api_key.txt` in the same directory as `simulate.py`. The file with your API key should contain *only* the API key and nothing else.

1. Install the OpenAI Python library by running `pip install openai` from the command line. 

## Adapting for other jobs

I've written this simulator to help me prepare for data science interviews, but it could easily be modified to prepare you for interviews in any other field. 

- Replace the predefined technical questions in the list `technical_questions` with questions that are relevant to your field.

- Replace 'data science' with your job field in the prompt sent to ChatGPT by the `serve_question()` function when requesting a single technical interview question (when `qtype == 'gt'` in the function).

- Replace the requests for lists of machine learning, stats/probability, and data science case study questions in the `serve_question()` function with requests for questions relevant to your field. Update the input codes and description in `qstr` as desired, making sure to update the input codes within `serve_question()` to match.
