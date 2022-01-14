pytest setup



Arrange
Act
Assert


happy path testing vs error testing


https://coverage.readthedocs.io/en/coverage-5.3/
pytest.ini ?!
+ bash

conftest.py for fixtures


testing
coverage
static
docs
setup


coverage:
coverage run { filename.py }
coverage report
coverage report --show-missing
coverage html

# testing coverage
pytest --cov
pytest --cov=tests/
pytest --cov=tests/ --cov-report=html
https://pytest-cov.readthedocs.io/en/latest/config.html

bash file:
#!/bin/sh
pytest --cov=tests/ --cov-report=html

mypy src\demo.py --html-report src