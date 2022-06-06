import abc
from pandas import DataFrame
from store.database import RedisController


class SignalDataManager(abc.ABC):
    """
    This manager is to manage signal data and interact with task queue.
    """

    def __init__(self):
        self.db = RedisController()

    def get(self, signal_name: str, begin: int, end: int) -> DataFrame:
        """
        在 redis 中查找表达式，返回因子值（初步实现）
        """
        raise NotImplementedError

    def put(self, signal_name: str, expression: str):
        """
        存入表达式至 redis / file
        """
        raise NotImplementedError


class SignalStorageManager(abc.ABC):
    """
    This manager is responsible for redis and meta-info managing.
    """

    def __init__(self):
        self.db = RedisController()

    def get(self, signal_name: str):
        raise NotImplementedError

    def put(self, signal_name: str, expression: str):
        raise NotImplementedError

    def scan(self):
        raise NotImplementedError
