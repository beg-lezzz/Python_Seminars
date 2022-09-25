# метод для запроса у пользователя целых чисел с проверкой на целочисленность
def input_int():
    try:
        num = int(input(f"Введите число: "))
        return int(num) if 0 < int(num) < 8 else quit(print('Ошибка. Вы ввели число, которому '
                                                           'не соответствует день недели.'))
    except ValueError:
        quit(print('Ошибка. Вы ввели не целое число.'))


# метод проверяет какой день недели соответствует введенному числу и проверяет выходной это день или будний
def check_day_number(day_number):
    day_list = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    if day_number in (6, 7):
        print(f"{day_list[day_number - 1]} - Выходной")
    else:
        print(f"{day_list[day_number - 1]} - Будний")


check_day_number(input_int())