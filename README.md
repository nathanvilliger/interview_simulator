# Job interview simulator

Use `simulate.py` to simulate data science job interviews from the command line.
The script serves up behavioral and technical questions from predefined lists
as requested by the user. It also includes the option to ask ChatGPT for sample
questions and answers! ChatGPT functionality requires a little setup; see below for details.

Good luck!

## Usage

Simply run `python simulate.py` from the command line to enter the simulator.

## ChatGPT setup

There's some quick setup that needs to be done before you can run the simulator and take advantage of the ChatGPT functionality. These steps are meant to be minimal and easy to follow; check out the [ChatGPT API documentation](https://platform.openai.com/docs/quickstart?context=python) for more information if you're interested.

1. Create an OpenAI account or sign in if you have one already.

1. Navigate to the [API key page](https://platform.openai.com/account/api-keys) and "Create new secret key."

1. Store the key in a file called `chatgpt_api_key.txt` in the same directory as `simulate.py`. The file with your API key should contain *only* the API key and nothing else.

1. Install the OpenAI Python library by running `pip install openai` from the command line. 

## Adapting for other jobs

I've written this simulator to help me prepare for data science interviews, but it could easily be modified to prepare you for interviews in any other field. Simply replace the predefined technical questions in the list `technical_questions` with questions that are relevant to your field and replace 'data science' with your job field in the prompt sent to ChatGPT by the `serve_question()` function.
