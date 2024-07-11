'''
Write a script to pop several questions from the predefined lists with one command rather than having to ask 
over and over again for one question at a time like in simulate.py. Ideally specify which list(s) and how many
questions as command line arguments; e.g. ask for 5 technical questions by running a command like
`python pop_several.py 5 t`

import simulate.py to bring in the variables and functions.

TO DO: create option to continue the "interview" beyond specified number of questions
rather than simply exiting
'''
import argparse
from random import shuffle
from subprocess import run

import simulate as sim

parser = argparse.ArgumentParser()
parser.add_argument('n', type=int, help='number of questions to draw from specified lists')
parser.add_argument('qtypes', help='which list or lists of questions to sample from? enter any combination of `t` '\
                    'for technical, `b` for behavioral, and `r` for resume')
args = parser.parse_args()

run('clear')

# check for validly-specified qtypes: needs to be `t` and/or `b` and/or `r`
# assemble list of requested questions
ops = ['t', 'b', 'r']
lists = ['technical_questions', 'behavioral_questions', 'resume_questions']
qlist = []
for o, l in zip(ops, lists):
    if o in args.qtypes:
        print(f'adding {l.replace("_", " ")}')
        qlist += eval(f'sim.{l}')
shuffle(qlist)

print(sim.divstr)
# for each question, serve and offer to ask GPT for sample answer
for i in range(args.n):
    q = qlist.pop()
    print(f'{i+1}. {q}')
    print(sim.divstr)

    request_answer = input('Would you like to request a sample answer from ChatGPT? y/n \n')
    if request_answer == 'y':
        print(sim.divstr)
        # request and print answer from GPT
        print(sim.prompt_gpt('Provide a sample answer to the following question: ' + q))

        # continue when user presses enter 
        _ = input('Press enter to continue. \n')

    run('clear')

print('All done. Good luck!')