import os

os.system('clear')
from models.add import *
from models.answer import *
from models.see import *
from models.question import *
from models.sql import *
from init_db import *

s = init_db_session('question.sqlite')


a = s.query(Question1).all()

print(a)