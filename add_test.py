import pytest

from models.add import Poll
from models.question import Question

class TestAdd:

    def test_question_storage(self):
        question1 = Question("What is your name?  ")
        poll= Poll(question= question1)

