import abc
import redis
from pandas import DataFrame


class SignalDataManager(abc.ABC):
    def __init__(self):
        pass

    def get(self, signal_name: str, begin: int, end: int) -> DataFrame:
        """
        首先去 redis 中查找表达式，其次全量计算，返回因子值（初步实现）
        """
        raise NotImplementedError

    def put(self, signal_name: str, expression: str):
        """
        存入表达式至 redis
        """
        raise NotImplementedError


class SignalStoreManager(abc.ABC):
    """
    This class is responsible for redis managing
    """

    def __init__(self, host: str = 'localhost', port: int = 6379, password: str = None):
        self.pool = redis.ConnectionPool(host, port)
        self.connection = redis.Redis(password=password, connection_pool=self.pool, decode_responses=True)

    def get(self, signal_name: str):
        raise NotImplementedError

    def put(self, signal_name: str, expression: str):
        raise NotImplementedError

    def scan(self):
        raise NotImplementedError
