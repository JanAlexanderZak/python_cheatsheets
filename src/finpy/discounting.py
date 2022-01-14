"""
Formula:
present_value = future_payment / ((1 + interest) ** year)
"""
import numpy as np
from typing import Union


class Discounting:
    def __init__(self):
        pass

    @staticmethod
    def future_payment(_interest, _present_value, _year) -> Union[float, int]:
        return _present_value * ((1 + _interest) ** _year)

    @staticmethod
    def interest(_future_payment, _present_value, _year) -> Union[float, int]:
        return (_future_payment / _present_value) ** (1 / _year) - 1

    @staticmethod
    def present_value(_future_payment, _interest, _year) -> Union[float, int]:
        return _future_payment / ((1 + _interest) ** _year)

    @staticmethod
    def year(_future_payment, _interest, _present_value) -> Union[float, int]:
        return np.log(_future_payment / _present_value) / np.log(1 + _interest)

    @staticmethod
    def present_value_wacc(_series_of_payments, wacc=0.05) -> Union[float, int]:
        _present_value = []
        for i, val in enumerate(_series_of_payments):
            # print(f"{val} / ((1 + 0.05) ** {i + 1}) = ", val / ((1 + 0.05) ** (i + 1)))
            # todo: get list of present values
            _present_value.append(val / ((1 + wacc) ** (i + 1)))
        return round(sum(_present_value), 5)

    @staticmethod
    def wacc(equity, debt, equity_cost, interest, tax) -> Union[float]:
        # equity cost is the return on capital in free market
        # interest is the similar cost for debt
        wacc = (equity / (equity + debt) * equity_cost) + (debt / (debt + equity) * interest) * (1 - tax)
        return wacc
