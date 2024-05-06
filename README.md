# Job interview simulator

Use `simulate.py` to simulate data science job interviews from the command line.
The script serves up behavioral, technical, and resume questions from predefined lists
as requested by the user. It also includes the option to ask ChatGPT for sample
questions and answers! ChatGPT functionality requires a little setup; see below for details.

Good luck!

## Usage

Simply run `python simulate.py` from the command line to enter the simulator. The application provides for two basic use patterns:

- Single questions at a time drawn from the predefined lists of questions stored in the `*_questions.txt` files.  

- Several questions in a row from ChatGPT. The code is currently written to ask for a list of five questions at a time in this mode, but that number could easily be changed by changing the prompts in the calls to `prompt_gpt()` within the `serve_question()` function (specifically the calls where `return_list=True`). (*Pro tip: quickly change the number of questions served by finding and replacing all instances of me having typed out 'five.'*)

You can modify the `*_questions.txt` files to make them more specific to you; in particular, definitely add a bunch of questions to `resume_questions.txt` that interrogate the things you claim to know in your resume. Just be sure to only write one question per line in any file so that the python script can correctly parse the questions you've added.  
(*See below for a tip if you want git to ignore the modifications you make.*) 

## ChatGPT setup

There's some quick setup that needs to be done before you can run the simulator and take advantage of the ChatGPT functionality. These steps are meant to be minimal and easy to follow; check out the [ChatGPT API documentation](https://platform.openai.com/docs/quickstart?context=python) for more information if you're interested.

1. Create an OpenAI account or sign in if you have one already.

1. Navigate to the [API key page](https://platform.openai.com/account/api-keys) and "Create new secret key."

1. Store the key the file `chatgpt_api_key.txt`, replacing `your_api_key` with your actual API key. The file with your API key should contain *only* the API key and nothing else.

1. Install the OpenAI Python library by running `pip install openai` from the command line. 

(*See below for a tip if you want git to ignore the modifications you make.*) 

## Adapting for other jobs

I've written this simulator to help me prepare for data science interviews, but it could easily be modified to prepare you for interviews in any other field. 

- Replace the predefined technical questions in the file `technical_questions.txt` with questions that are relevant to your field.

- In `simulate.py`, replace the requests for lists of machine learning, stats/probability, and data science case study questions in the `serve_question()` function with requests for questions relevant to your field. Update the input codes and description in `qstr` as desired, making sure to update the input codes within `serve_question()` to match.

## Git tip

Here's a method for including files in a repo that are intended to be changed, but you *don't* want the changes to show up every time you run `git status` nor do you want changes to be accidentally overwritten by a future `git pull`. You can run  
`git update-index --skip-worktree <filename>`  
to make git act as if the file has not been modified even if it has been. I found this method on [this](https://stackoverflow.com/questions/13630849/git-difference-between-assume-unchanged-and-skip-worktree#) Stack Overflow page, and you can read directly from the git documentation [here](https://git-scm.com/docs/git-update-index#:~:text=skip%2Dworktree%20tells%20Git%20to,absence%20be%20recorded%20in%20commits.)

I ran this command for two files: `chatgpt_api_key.txt` and `resume_questions.txt`. I wanted to include skeleton versions of each file in the Github repo, but both are intended to be changed upon a user cloning the repo. Using the command means I don't accidentally commit and push my personal API key or questions that are specific to my resume. It also prevents those modified files from annoyingly showing up as having been modified every time I run `git status`.