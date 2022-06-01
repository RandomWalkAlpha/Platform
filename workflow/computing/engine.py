import celery
from celery import Celery, Task
from data.store.database import RedisController
from datetime import datetime
from pandas import DataFrame
from utils.mapping import MAPPING_FUNCTION_SET, DELAY, DELTA, MA, RANK, RETURN, STD


class ComputingEngine(Task):

    def __init__(self, data_std: DataFrame):
        # self.celery = Celery('engine', backend='redis://localhost', broker='redis://localhost//6379')
        # self.db = RedisController()
        self.data = data_std

    def expression_parse(self, expression: str) -> (str, DataFrame, int):
        """
        EXPRESSION is combined with function, variable.
         eg: 'MA($close, 3)' means computing the 3-day moving average using closing price
        """
        subset = ['zs_trading_day', 'zs_code']
        field = expression[expression.find('$') + 1: expression.find(',')]
        dataframe = self.data.drop_duplicates(subset=subset)
        trading_day_series = dataframe.copy()
        trading_day_series.loc[:, 'zs_trading_day'] = trading_day_series.loc[:, 'zs_trading_day'] * 10000 + 1600
        op = expression[:expression.find('(')]
        assert op in MAPPING_FUNCTION_SET, "Add meta function name to MAPPING_FUNCTION_SET and implement it."
        data = trading_day_series.pivot(index='zs_trading_day', columns='zs_code', values=field)
        days = int(expression[expression.find(',') + 1: expression.find(')')])
        return op, data, days

    def compute(self, expression: str) -> (DataFrame, datetime):
        start_time = datetime.now()
        op, data, days = self.expression_parse(expression)
        result = eval(op)(data, days)
        end_time = datetime.now()
        cost_time = end_time - start_time
        return result, cost_time

    def record(self):
        pass
