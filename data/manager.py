import abc
import pickle
from pandas import DataFrame
from typing import Optional, Dict
from store.database import RedisController


class SignalDataManager(abc.ABC):
    """
    This manager is to manage signal data and interact with task queue.
    """

    def __init__(self):
        self.db = RedisController()

    def get(self, signal_name: str, begin: int, end: int) -> DataFrame:
        data_bytes = self.db.get(f'signal_data:{signal_name}')
        dataframe = pickle.loads(data_bytes)
        df = dataframe.loc[begin: end, :]
        return df

    def put(self, signal_name: str, dataframe: DataFrame):
        data_bytes = pickle.dumps(dataframe)
        self.db.put(f'signal_data:{signal_name}', data_bytes)


class SignalStorageManager(abc.ABC):
    """
    This manager is responsible for redis and signal expressions managing.
    """

    def __init__(self):
        self.db = RedisController()
        self.signal_notes = {}

    def get(self, signal_name: str) -> str:
        return self.db.get(f'signal:{signal_name}')

    def put(self, signal_name: str, expression: str, notes: str = ''):
        self.db.put(f'signal:{signal_name}', expression)
        self.signal_notes[f'signal:{signal_name}'] = notes

    def scan(self) -> Optional[Dict]:
        return self.signal_notes
