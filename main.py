import os

os.system('clear')
from models.add import *
from models.answer import *
from models.see import *
from models.question import *
from models.sql import *
from init_db import *

s = init_db_session('question.sqlite')


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

                if intnumber == 1:
                  multiplechoice = MultipleChoice(answernumber=intnumber)
                  multiplechoice.askanswer()
                  potentialanswer = PotentialAnswer(name= multiplechoice.allanswers[0])
                  s.add(potentialanswer)
                  s.commit()
                elif intnumber == 2:
                  multiplechoice = MultipleChoice(answernumber=intnumber)
                  multiplechoice.askanswer()
                  potentialanswer = PotentialAnswer(name= multiplechoice.allanswers[0], name1= multiplechoice.allanswers[1])
                  s.add(potentialanswer)
                  s.commit()
                elif intnumber == 3:
                  multiplechoice = MultipleChoice(answernumber=intnumber)
                  multiplechoice.askanswer()
                  potentialanswer = PotentialAnswer(name= multiplechoice.allanswers[0], name1= multiplechoice.allanswers[1], name2= multiplechoice.allanswers[2])
                  s.add(potentialanswer)
                  s.commit()
                elif intnumber == 4:
                  multiplechoice = MultipleChoice(answernumber=intnumber)
                  multiplechoice.askanswer()
                  potentialanswer = PotentialAnswer(name= multiplechoice.allanswers[0], name1= multiplechoice.allanswers[1], name2= multiplechoice.allanswers[2],name3= multiplechoice.allanswers[3])
                  s.add(potentialanswer)
                  s.commit()
                else:
                  print("You entered too many questions")
                print("Your question has been created!")

else:
    print("OK see you later!")


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
            print("The following polls are available to launch")
            a = s.query(Question1).all()
            for i in a:
              print(i.id, i.rt)
            whichpoll = int(input("Select the ID of the poll you would like to launch: (int) "))
            whichpoll = whichpoll - 1
            print("Answer the following question?")
            print(s.query(Question1)[whichpoll].rt, "?")
            q_id = s.query(PotentialAnswer)[whichpoll].id
            dicti = {1 : s.query(PotentialAnswer)[q_id].name,
                     2 : s.query(PotentialAnswer)[q_id].name1,
                     3 : s.query(PotentialAnswer)[q_id].name2,
                     4 : s.query(PotentialAnswer)[q_id].name3}
            print(dicti)
            whichchoice = int(input(("Select the number corresponding to your answer (int) ")))
            print(whichchoice)
            print("You have selected " + dicti[whichchoice])
            #### THIS PART DOES NOT WORK
            #actualanswer = ActualAnswer(qid= q_id, answer = dicti[whichchoice])
            #s.add(actualanswer)
            #s.commit()

            polllaunch == True

            break
        else:
            print("No poll is being launched, have a nice day!")
            polllaunch= False
            break
