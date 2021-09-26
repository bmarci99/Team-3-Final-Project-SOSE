import os

os.system('clear')
from models.add import *
from models.answer import *
from models.see import *
from models.question import *
#import pandas as pd

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
        QA = YesNoAnswers()
    elif yesnotype.istype == "N":
        tries = True
        tres = 0
        while tries == True:
            try:
                intnumber = int(input("How many answers? (int) "))
            except:
                if tres < 2:
                    print("Invalid input. Please enter an integer")
                    tres += 1
                    continue
                elif tres == 2:
                    print("To many invalid inputs. Question has not been created")
                    break
            else:
                tries = False
                multiplechoice = MultipleChoice(answernumber=intnumber)
                multiplechoice.askanswer()
                QA = MCAnswers(answers = multiplechoice.allanswers)
                print("Your question has been created!")

else:
    print("OK see you later!")

polllaunch = True
pollfail= 0

launchpoll = input("Do you want to launch a poll? (Y/N) ")
launchpoll = str(launchpoll).capitalize()

while polllaunch==True and pollfail<=3:
    try:
        len(launchpoll) == 1
    except:
        print("Invalid input, please respond with Y or N")
        pollfail += 1
        if pollfail >3:
            print("Sorry too many failed attempts!")
    else:
        if launchpoll == "Y":
            whichpoll = input("Which poll would you like to launch? (int) ")
            break
        else:
            print("No poll is being launched, have a nice day!")
            polllaunch= False

