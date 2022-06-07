from celery import Task
from datetime import datetime
from pandas import DataFrame
from utils.mapping import MAPPING_FUNCTION_SET, DELAY, DELTA, MA, RANK, RETURN, STD
from data.collector.collector import DQCollector
from data.manager import SignalDataManager, SignalStorageManager


class ComputingEngine(Task):
    """
    This engine is used to arrange data and computing.
    Now we have registered this class to 'celery' so that engine could get the task computed.
    """

    def __init__(self):
        self.collector = DQCollector()
        self.sdm = SignalDataManager()
        self.ssm = SignalStorageManager()

    def expression_parse(self, expression: str) -> (str, DataFrame, int):
        """
        EXPRESSION is combined with function, variable.
         eg: 'MA($close, 3)' means computing the 3-day moving average using closing price
        """
        field = expression[expression.find('$') + 1: expression.find(',')]
        op = expression[:expression.find('(')]
        assert op in MAPPING_FUNCTION_SET, "Add meta function name to MAPPING_FUNCTION_SET and implement it."
        data = self.collector.standardize(index='zs_trading_day', columns='zs_code', values=field)
        days = int(expression[expression.find(',') + 1: expression.find(')')])
        return op, data, days

    def compute(self, expression: str) -> (DataFrame, datetime):
        start_time = datetime.now()
        op, data, days = self.expression_parse(expression)
        result = eval(op)(data, days)
        end_time = datetime.now()
        cost_time = end_time - start_time
        return result, cost_time

    def to_redis(self, result: DataFrame, name: str, expression: str, notes: str = ''):
        self.sdm.put(name, result)
        self.ssm.put(name, expression, notes)

    def to_file(self, result: DataFrame, path: str = './', name: str = 'data', key: str = 'hdf'):
        result.to_hdf(f'{path}{name}.hdf', key=key)
