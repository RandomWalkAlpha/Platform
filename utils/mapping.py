import numpy as np
from pandas import DataFrame
"""
The following 'data' in function parameters refers to standardized dataframe
"""

MAPPING_FUNCTION_SET = (
    'DELAY',
    'DELTA',
    'MA',
    'RANK',
    'RETURN',
    'STD',
)


def DELAY(data: DataFrame, days: int) -> DataFrame:
    return data.shift(days)


def DELTA(data: DataFrame, days: int) -> DataFrame:
    return data.diff(days)


def MA(data: DataFrame, days: int) -> DataFrame:
    return data.rolling(days).mean()


def RANK(data: DataFrame, days: int) -> DataFrame:
    daily_return = RETURN(data, days)
    ranking_data_frame = DataFrame(index=daily_return.index, columns=daily_return.columns)
    code_query = {v: k for k, v in enumerate(daily_return.columns)}
    for date in ranking_data_frame.index:
        return_list = daily_return.loc[date, :]
        ranking_tuple_list = sorted([*zip(code_query.keys(), return_list)], key=lambda x: -x[1])
        rank_list = [np.nan] * len(code_query.keys())
        rank = 1
        for c, _ in ranking_tuple_list:
            if not np.isnan(_):
                rank_list[code_query[c]] = rank
                rank += 1
        ranking_data_frame.loc[date, :] = rank_list
    return ranking_data_frame


def RETURN(data: DataFrame, days: int) -> DataFrame:
    n_days_return = (data - data.shift(days)) / data.shift(days)
    return n_days_return


def STD(data: DataFrame, days: int) -> DataFrame:
    return data.rolling(days).std()