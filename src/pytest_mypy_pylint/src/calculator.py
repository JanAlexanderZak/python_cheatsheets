import numbers


class CalculatorError(Exception):
    pass


class Calculator:
    """
    A calculator
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def add(self, x, y):
        self._check_operand(x)
        self._check_operand(y)
        return x + y

    def subtract(self):
        return self.x - self.y

    @staticmethod
    def _check_operand(operand):
        if not isinstance(operand, numbers.Number):
            raise CalculatorError('{operand} is not a number'.format(operand=operand))