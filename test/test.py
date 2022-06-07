import pandas as pd
from pandas import DataFrame
from data.collector.collector import DQCollector
from utils.task import ComputingTask
import pickle

collector = DQCollector()

task = collector.standardize(index='zs_trading_day', columns='zs_code', values='S_DQ_CLOSE')
print(task)
x = pickle.dumps(task)
y = pickle.loads(x)
print(y)

'''
from celery import Celery
app = Celery('hello', backend='redis://localhost', broker='redis://localhost//6379')

@app.task
def hello():
    return 'hello world'

from utils.mapping import *
from workflow.computing.engine import ComputingEngine
from data.collector.collector import DQCollector
'''

'''
def store(result: DataFrame, **kwargs):
    result.to_hdf(f"{kwargs['name']}.hdf", key=kwargs['key'])

engine = ComputingEngine()
result, _ = engine.compute("MA($S_DQ_CLOSE,5)")
dic = {'name': 'test', 'key': 'df'}
store(result, **dic)
'''
