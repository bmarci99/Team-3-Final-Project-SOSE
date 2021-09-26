import os

os.system('clear')
from models.add import *
from models.answer import *
from models.see import *
from models.question import *

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%% S U R V E Y %%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")

question_options= input("Do you want to create a Poll? (response: Y/N) ")

if question_options.capitalize()=="Y":
    question= input("What is your question?  ")
    poll= Poll(question)
    yesnotype = str(input("Is this a Yes or No question? (responses: Y/N) ")).capitalize()
    yesnotype = YesNo(istype=yesnotype)
    if yesnotype.istype == "Y":
        print("This is a Yes or No question")
    else:
        print("This is a multiple choice question")
else:
    print("OK see you later!")