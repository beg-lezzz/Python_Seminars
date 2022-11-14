import datetime
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time_ns()
        res = func(*args, **kwargs)
        finish_time = time.time_ns()
        exec_time = finish_time - start_time
        return res, exec_time

    return wrapper


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
        log_msg += f'Функция: {func.__name__}\t'
        log_msg += f"Переданы параметры: {', '.join(map(str, args))}\t"
        res = func(*args, **kwargs)
        log_msg += f'Результат выполнения: {res[0]}\t'
        log_msg += f'Время выполнения: {res[1]}\n'
        with open('log_file.log', 'a+', encoding='utf8') as fp:
            fp.write(log_msg)
        return res

    return wrapper


def cacher(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        key = args
        if key not in cache:
            cache[key] = func(*args)
        return cache[key]

    return wrapper


@logger
@timer
@cacher
def seq(n):
    result = []
    for i in range(n):
        res = (1 + i) ** i
        result.append(res)

    return result


def main():
    seq(2000)
    seq(3000)
    seq(2000)
    seq(4000)
    seq(2000)
    seq(1000)
    seq(4000)
    seq(500)


if __name__ == '__main__':
    main()
