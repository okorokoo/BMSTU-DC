from functools import wraps
import datetime
from inspect import getcallargs

logger = []     # этот словарь будет хранить наш "лог"


def logging_decorator(logger: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = datetime.datetime.now()
            result = func(*args, **kwargs)
            d = {'name': func.__name__, 'arguments': getcallargs(func, *args, **kwargs), 'call_time': start,
                 'result': result}
            logger.append(d)
            return result
        return wrapper
    return decorator


@logging_decorator(logger)  # в аргументы фабрики декораторов подается логгер
def test_simple(a, b=2):
    return 127


test_simple(1)  # при вызове функции в список logger должен добавиться словарь с
                # информацией о вызове функци

print(logger)