from abc import ABCMeta, abstractmethod
from typing import Dict


class Task(metaclass=ABCMeta):
    """
    Abstract base class
    """

    @abstractmethod
    def get_compute_expr(self, *args, **kwargs): ...


class ComputingTask(Task):
    """
    Class for computing task
    """
    def __init__(self, config: Dict):
        """
        :param config: Dict
        """
        self.expression = config['expression']
        self.name = config['name']

    def get_compute_expr(self) -> str:
        return self.expression
