import os

os.system('clear')
from models.add import *
from models.answer import *
from models.see import *

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%% S U R V E Y %%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")


question_options= input("Do you want to create a Poll? (response: Y/N)")
    if question_options=="Y":
        question= input("What is your question?  ")
        poll= Poll(question)
    else:
        print("OK see you later!")