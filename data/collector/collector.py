from abc import ABCMeta, abstractmethod
from pandas import DataFrame
from pandas import read_parquet


class Collector(metaclass=ABCMeta):
    """
    Abstract base class
    """

    @abstractmethod
    def read(self, *args, **kwargs): ...

    @abstractmethod
    def write(self, *args, **kwargs): ...


class DQCollector(Collector):
    """
    Data collector for daily quotation
    """

    def __init__(self, data_path: str = "../2015.parquet"):
        self.dq_path = data_path
        self.quotation = None
        self.read()

    def read(self):
        df = read_parquet(self.dq_path)
        self.quotation = df

    def write(self, data: DataFrame, dst: str, key: str = '') -> bool:
        try:
            data.to_hdf(dst, key=key)
            return True
        except IOError:
            return False

    def standardize(self, index, columns=None, values=None, subset=None) -> DataFrame:
        """
        To convert raw daily quotation to standard format
        """
        if subset is None:
            subset = ['zs_trading_day', 'zs_code']
        dataframe = self.quotation.drop_duplicates(subset=subset)
        trading_day_series = dataframe.copy()
        trading_day_series.loc[:, 'zs_trading_day'] = trading_day_series.loc[:, 'zs_trading_day'] * 10000 + 1600
        return trading_day_series.pivot(index=index, columns=columns, values=values)
