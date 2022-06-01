from pandas import DataFrame
from utils.task import ComputingTask
import pickle
'''
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
'''
from utils.mapping import *
from workflow.computing.engine import ComputingEngine
from data.collector.collector import DQCollector

engine = ComputingEngine()
result, _ = engine.compute("MA($S_DQ_CLOSE,5)")
print(result, _)