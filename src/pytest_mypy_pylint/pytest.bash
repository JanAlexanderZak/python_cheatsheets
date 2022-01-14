#!/bin/bash

pytest --cov=tests/ --cov-report=html pytest/
mypy --config-file=mypy.ini src\demo.py --html-report mypy
pylint --rcfile=.pylintrc
