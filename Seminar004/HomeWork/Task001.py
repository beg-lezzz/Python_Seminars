# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141 10-1 <= d <= 10-10


import math


# метод для запроса у пользователя чисел с проверкой на условия
def input_int():
    try:
        num = input(f"Введите число, обозначающее точность округления: ")
        return num[:-1] + '1' if math.pow(10, -10) <= float(num) <= math.pow(10, -1) else \
            quit('Ошибка. Введите вещественное число в диапазоне от 10^-10 до 10^-1.')
    except ValueError:
        quit('Ошибка. Введите вещественное число в диапазоне от 10^-10 до 10^-1.')


# метод для вывода числа Пи с заданной точностью
def pow_pi(num):
    # рассчитываем коэффициент для вычисления с заданной точностью - единицу делим на введенное число
    # и округляем до целого
    k = int(round(1/float(num), 0))
    # возвращаем кортеж из числа Пи, математически посчитанного результата и результата через округление
    # до количества знаков = количеству знаков после "." во введенном числе
    return math.pi, int(math.pi * k) / k, round(math.pi, len(num.split('.')[1]))


def main(input_data):
    print('\n' + '*' * 21 + ' Число Пи ' + '*' * 22 + '\n' + str(input_data[0])+ '\n' * 2
          + '*' * 14 + ' Результат математически ' + '*' * 14 + '\n' + str(input_data[1]) + '\n' * 2
          + '*' * 15 + ' Результат округлением ' + '*' * 15 + '\n' + str(input_data[2]) + '\n')


main(pow_pi(input_int()))
