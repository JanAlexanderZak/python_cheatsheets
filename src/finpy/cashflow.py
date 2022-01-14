import pandas as pd
import plotly.express as px
import numpy as np
from typing import Tuple, Union


class Cashflow:
    def __init__(self, profit: pd.Series, depreciation: pd.Series, running_cost: pd.Series, debt: pd.Series):
        self.profit = profit
        self.depreciation = depreciation
        self.running_cost = running_cost
        self.debt = debt

    @staticmethod
    def cashflow_and_profit(
            cash_profit: Union[int, float],
            non_cash_profit: Union[int, float],
            cash_expense: Union[int, float],
            non_cash_expense: Union[int, float]) -> Tuple[Union[int, float], Union[int, float]]:
        """ Calculate cashflow and profit
        :param cash_profit: cash
        :param non_cash_profit: eg. claims from suppliers
        :param cash_expense: cash
        :param non_cash_expense: eg. demands from suppliers
        :return: cashflow, profit
        """
        cashflow = cash_profit - cash_expense
        profit = cashflow + (non_cash_profit - non_cash_expense)
        return cashflow, profit

    def debt_capacity(self) -> Union[int, float]:
        return 7 * self.free_cashflow() - np.average(self.debt)

    def free_cashflow(self) -> Union[int, float]:
        return self.average_cashflow() - np.average(self.running_cost)

    def average_cashflow(self) -> Union[int, float]:
        return np.average(self.profit + self.depreciation)


if __name__ == '__main__':
    # todo: different dfs...
    # Visualize 1
    df = pd.DataFrame(
        [['Company A', '2000', 50, 10, 30, 10],
         ['Company A', '2001', 55, 20, 29, 20],
         ['Company A', '2002', 65, 20, 31, 20], ],
        columns=['Company', 'Year', 'Profit', 'Depreciation', 'Running Cost', 'Debt'])

    fig = px.bar(df, x='Year', y=['Profit', 'Depreciation'], title="Wide-Form Input")
    fig.update_layout(xaxis=dict(type='category'))
    fig.show()

    # Visualize 2
    df = pd.DataFrame(
        [['Company A', 'profit', 100, 50],
         ['Company A', 'expense', 80, 40], ],
        columns=['Company', 'Profit/Expense', 'Cash', 'Non_Cash'])

    fig = px.bar(df, x='Profit/Expense', y=['Cash', 'Non_Cash'], title="Wide-Form Input")
    fig.update_layout(xaxis=dict(type='category'))
    fig.show()
