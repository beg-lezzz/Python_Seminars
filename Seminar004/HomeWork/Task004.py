# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random


# метод для запроса у пользователя чисел с проверкой на условия
def input_int():
    try:
        num = int(input(f"Введите число элементов списка: "))
        return num if num > 0 else \
            quit('Ошибка. Введите целое число больше 1.')
    except ValueError:
        quit('Ошибка. Введите целое число больше 1.')


# метод возвращает случайное число от 0 до 100
def fill_list_rnd():
    return random.randint(0, 3)


# метод для составления многочлена с количеством слагаемых = введенному пользователем
def fill_polynomial(input_num):
    sum_list = []
    for i in range(input_num + 1):
        k = fill_list_rnd()
        if k == 0:
            continue
        else:
            sum_list.insert(0, str(k)) if i == 0 \
                else sum_list.insert(0, str(k) + 'x') if i == 1 \
                else sum_list.insert(0, str(k) + 'x^' + str(i))

    return " + ".join(sum_list) + ' = 0'


print(fill_polynomial(input_int()))
