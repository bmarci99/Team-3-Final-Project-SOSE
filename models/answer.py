class Answer():
    def __init__(self, answers = []):
        Answer.answers = answers

class YesNoAnswers(Answer):
    def __init__(self, answers = ['Y', 'N']):
        self.answers = answers

    def __repr__(self):
        return self.answers

class MCAnswers(Answer):
    def __init__(self, answers = []):
        self.answers = answers
    def Call(self):
        print(self.answers)