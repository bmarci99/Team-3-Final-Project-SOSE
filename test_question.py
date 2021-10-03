import pytest
from models.question import *

class TestQuestion:
    def test_yesno_question(self):
        question2 = YesNo("Y")
        assert question2.istype == "Y"

    def test_multiplechoice(self):
        question3= MultipleChoice(3)
        assert question3.answernumber == 3
