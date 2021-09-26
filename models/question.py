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

