#created a question class

class Question:
    def __init__(self, query):
        self.query = query

    def __repr__(self):
        return self.query
