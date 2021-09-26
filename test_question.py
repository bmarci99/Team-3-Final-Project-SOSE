import pytest

from models.question import *

class TestQuestion:
    def test_yesno_question(self):
        question2 = YesNo("Y")
        assert question2== "Y"

    def test_multiplechoice(self):
        question3= MultipleChoice(3)
        assert len(question3.askanswer())==3
