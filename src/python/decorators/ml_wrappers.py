import functools


def model_required(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        if args[0].model:
            return func(*args, **kwargs)
        else:
            print('No model')
    return _wrapper


def data_required(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        if args[0].loaded:
            return func(*args, **kwargs)
        else:
            print('No data')
    return _wrapper

