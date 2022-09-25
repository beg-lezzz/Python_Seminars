#метод для запроса у пользователя целых чисел с проверкой на целочисленность
def input_int():
    try:
        num = int(input(f"Введите номер четверти: "))
        return int(num) if 0 < int(num) < 5 else quit(print('Ошибка. Вводить необходимо числа от 1 до 4'))
    except ValueError:
        quit(print('Ошибка. Вы ввели не целое число.'))


# метод для вывода условий для координат X и Y по введенному номеру четверти координатной плоскости
def find_quarter(num_quarter):

    return "x > 0, y > 0" if num_quarter == 1 else \
            "x > 0, y > 0" if num_quarter == 2 else \
            "x > 0, y > 0" if num_quarter == 3 else \
            "x > 0, y > 0" if num_quarter == 4 else \
            "Ошибка"


print(find_quarter(input_int()))
