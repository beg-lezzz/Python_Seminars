import random
# метод для запроса у пользователя целых чисел с проверкой на целочисленность
def input_int():
    try:
        num = int(input(f"Введите число: "))
        return int(num) if int(num) > 0 else quit(print('Ошибка. Введите число больше нуля.'))
    except ValueError:
        quit(print('Ошибка. Вы ввели не целое число.'))


# метод для заполнения списка длины N числами от 1 через дальнейшее умножение на -3
def fill_list(input_number):
    list = []
    i = 0
    r = 1
    while i <= input_number:
        list.insert(i, r)
        r *= (-3)
        i += 1
    return list


print(*fill_list(input_int()), sep = ', ')
