import os

os.system('clear')
from models.add import *
from models.answer import *
from models.see import *
from models.question import *
from models.sql import *
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

engine = create_engine(
    'sqlite:///OurDataBase.sqlite',
    connect_args ={"check_same_thread": False},
    poolclass=StaticPool
)
Base = declarative_base()
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
s = session()

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%% S U R V E Y %%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")

question_options= input("Do you want to create a Poll? (response: Y/N) ")
if question_options.capitalize()=="Y":
    question= input("What is your question?  ")
    value= Question1(rt=question)
    s.add(value)
    s.commit()
    poll= Poll(question)
    yesnotype = str(input("Is this a Yes or No question? (responses: Y/N) ")).capitalize()
    yesnotype = YesNo(istype=yesnotype)
    if yesnotype.istype == "Y":
        QA = YesNoAnswers()
        potentialanswer = PotentialAnswer(name= 'Y', name1 = 'N')
        s.add(potentialanswer)
        s.commit()
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

<<<<<<< HEAD

a = s.query(Question).all()

for i in a:
    print(i.rt)

polllaunch = True
=======
>>>>>>> 441fd7e3d0931c3edb59446d8f11da4ab659ccfd
pollfail= 0
polllaunch= True

launchpoll = input("Do you want to launch a poll? (Y/N) ")
launchpoll = str(launchpoll).capitalize()

while True and pollfail<=3:
    try:
        len(launchpoll) == 1
    except:
        print("Invalid input, please respond with Y or N")
        pollfail += 1
        if pollfail >3:
            print("Sorry too many failed attempts!")
            polllaunch==False
            break
    else:
        if launchpoll == "Y":
            whichpoll = input("Which poll would you like to launch? (int) ")
            polllaunch == True
            break
        else:
            print("No poll is being launched, have a nice day!")
            polllaunch= False
            break

if polllaunch==True:








