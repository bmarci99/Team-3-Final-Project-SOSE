#created a question class

class Question:
    def __init__(self, query):
        self.query = query

    def __repr__(self):
        return self.query

class YesNo(Question):
    def __init__(self, istype = "Y"):
        self.istype = istype

class MultipleChoice(Question):
    def __init__(self, answernumber = 4):
        self.answernumber = answernumber

    def askanswer(self):
        allanswers = []
        for i in range(1, (self.answernumber + 1)):
            promptanswer = str(input("What would you like answer number {} to be? ".format(i)))
            allanswers.append(promptanswer)
            i += 1
        self.allanswers = allanswers
        return allanswers

