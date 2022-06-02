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
    Class for computing task.
    This class is designed for adding tasks with config files.
    Now we have implemented factor computing due to simple expression inputting.
    """
    def __init__(self, config: Dict):
        """
        :param config: Dict
        """
        self.expression = config['expression']
        self.name = config['name']

    def get_compute_expr(self) -> str:
        return self.expression
