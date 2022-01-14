from finpy.discounting import Discounting


class Dividends:
    def __init__(self):
        pass

    @staticmethod
    def dividend_yield(dividend, stock_value, interest, years):
        """ Dividend yield until sold in n years"""
        discount = Discounting()
        _present_value = []
        yearly_dividend = stock_value * dividend
        for i in range(1, years + 1):
            _present_value.append(discount.present_value(yearly_dividend, interest, i))
        _present_value.append(discount.present_value(stock_value, interest, years))
        return _present_value

    @staticmethod
    def earnings_yield(profit_per_stock, stock_value):
        return profit_per_stock / stock_value
