from question import Question

#create a poll class
class Poll:

    def __init__(self):
        pass

#store the question as a method so it can be called as text
    def question(self, as_text=False):
        if as_text == True:
            question_as_text = self._question
            return question_as_text
        else:
            return self._question
