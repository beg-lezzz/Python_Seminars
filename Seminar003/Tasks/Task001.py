import time


# метод для запроса у пользователя целых чисел с проверкой на целочисленность
def input_int():
    try:
        num = int(input(f"Введите количество символов в случайном числе: "))
        return int(num) if 0 < int(num) < 16 else quit('Ошибка. Генерируется число от 1 до 15 символов')
    except ValueError:
        quit(print('Ошибка. Вы ввели не целое число.'))


# метод для генерации случайного числа из заданного количества символов
def rnd_nums(count_digits):
    rnd_num = str(time.time()).replace('.', '')[-count_digits:]
    return int(rnd_num) if rnd_num[0] != '0' else int(rnd_num) * 10


print(f'Случайное число = {rnd_nums(input_int())}')
