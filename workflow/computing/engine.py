from celery import Celery
from data.store.database import RedisController


class ComputingEngine:
    def __init__(self):
        # TODO: to deal self.queue with celery
        self.celery = Celery('engine', backend='redis://localhost', broker='redis://localhost//6379')
        self.db = RedisController()

    def expression_parse(self, expression: str):
        """
        EXPRESSION is combined with function, variable.
         eg: 'MA($close, 3)' means computing the 3-day moving average using closing price
        """
        pass

    def compute(self):
        pass

    def record(self):
        pass
