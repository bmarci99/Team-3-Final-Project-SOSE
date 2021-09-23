import pytest

from add import Poll
from question import Question

class TestAdd:

    def test_question_storage(self):
        question1 = Question("What is your name?  ")
        poll= Poll(question= question1)

