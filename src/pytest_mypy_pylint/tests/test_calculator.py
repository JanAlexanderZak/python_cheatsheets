from src.calculator import Calculator, CalculatorError
import pytest


def test_add():
    calculator = Calculator(2, 3)

    result = calculator.add(2, 3)
    assert result == 5


def test_subtract():
    calculator = Calculator(9, 3)

    result = calculator.subtract()
    assert result == 6


def test_add_weird_stuff():
    calculator = Calculator(2, 2)

    with pytest.raises(CalculatorError) as context:
        result = calculator.add('two', 'three')
        print(result)

    assert str(context.value) == "two is not a number"


