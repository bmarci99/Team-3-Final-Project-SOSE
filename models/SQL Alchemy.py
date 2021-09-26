from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Question(Base):
    __tablename__ = 'Question'
    id = Column(Integer, primary_key=True)
    question = Column(String)


class PotentialAnswer(Base):
    __tablename__ = 'Potential_Answers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    Question_id = Column(Integer, ForeignKey('Question.id'))
    potentialanswer = relationship(Question, backref=backref('potential_answer', uselist=True))


class ActualAnswer(Base):
    __tablename__ = 'Answers'
    id = Column(Integer, primary_key=True)
    answer = Column(Integer)
    Potential_Answers_id = Column(Integer, ForeignKey('Potential_Answers.id'))
    actualanswer = relationship(PotentialAnswer, backref=backref('actual_answer', uselist=True))
