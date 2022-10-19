from datetime import datetime as dt


def calc_logger(math_expression, result):
    time = dt.now().strftime('%d.%m.%y - %H:%M:%S')
    with open('log.csv', 'a') as log_file:
        log_file.write(f'{time} = > {math_expression} = {result}\n')
