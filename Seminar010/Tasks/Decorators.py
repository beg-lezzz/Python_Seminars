import datetime
from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
        log_msg += f'Функция: {func.__name__}\t'
        log_msg += f"Параметры: {', '.join(map(str, args))}\t"
        res = func(*args, **kwargs)
        log_msg += f'Результат: {res}\n'
        print(log_msg)
        with open('log_file.log', 'a', encoding='utf8') as fp:
            fp.write(log_msg)
        return res

    return wrapper


def log_func(log_lvl=0):
    def logger2(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
            if log_lvl >= 1:
                log_msg += f'Функция: {func.__name__}\t'
                if log_lvl == 2:
                    log_msg += f"Параметры: {', '.join(map(str, args))}\t"
            res = func(*args, **kwargs)
            log_msg += f'Результат: {res}\n'
            print(log_msg)
            with open('log_file.log', 'a', encoding='utf8') as fp:
                fp.write(log_msg)
            return res

        return wrapper
    return logger2


def html_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        log_msg = '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Title</title></head><body>'
        log_msg += f"Комната {' на '.join(map(str, args))}\t"
        log_msg += f'Площадь комнаты: {res} м2 </body></html>\n'
        with open('log_file.html', 'a', encoding='utf8') as fp:
            fp.write(log_msg)
        # print(f'Площадь комнаты = {res} м2')
        return res

    return wrapper


def cacher(func):
    cach = {}
    @wraps(func)
    def wrapper(*args):
        res = func(*args)
        key = args
        if key not in cach:
            cach[key] = func(*args)
        print(cach)
        return cach[key]
    return wrapper


@cacher
def area_room(x, y):
    """
    Функция возвращает площадь комнаты
    :param x:
    :param y:
    :return:
    """
    return x * y


def main():
    print(area_room(5, 4))
    print(area_room(1, 3))
    print(area_room(7, 6))
    print(area_room(5, 4))
    print(area_room(5, 4))


if __name__ == '__main__':
    main()


# @html_decorator
# def area_room(x, y):
#     return x * y
#
#
# print(area_room(5, 3))


def timer():
    def wrapper():
        pass
