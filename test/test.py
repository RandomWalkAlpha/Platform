from pandas import DataFrame
from utils.task import ComputingTask
import pickle

conf = {'expression': '1', 'name': 'xyz'}

data = DataFrame()
task = ComputingTask(conf, data)
x = pickle.dumps(task)
print(x, type(x))
y = pickle.loads(x)
print(y, type(y))

from celery import Celery
app = Celery('hello', backend='redis://localhost', broker='redis://localhost//6379')

@app.task
def hello():
    return 'hello world'
