from models.answer import *

def test_answer():
    answerlist = ["Agree", "Neutral", "Disagree"]
    answertry = MCAnswers(answerlist)
    assert answertry.answers == ["Agree", "Neutral", "Disagree"]