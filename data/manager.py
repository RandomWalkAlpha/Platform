from abc import ABCMeta, abstractmethod
from pandas import DataFrame

class Manager(metaclass=ABCMeta):
    """
    Abstract base class
    """

    @abstractmethod
    def get(self, *args, **kwargs): ...

    @abstractmethod
    def put(self, *args, **kwargs): ...


class SignalDataManager(Manager):
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


class SignalDefinitionManager(Manager):
    """
    此类用于与 redis 的交互
    # TODO: 解耦
    """
    def __init__(self):
        pass

    def get(self, *args, **kwargs):
        raise NotImplementedError

    def put(self, *args, **kwargs):
        raise NotImplementedError

    def scan(self):
        raise NotImplementedError
