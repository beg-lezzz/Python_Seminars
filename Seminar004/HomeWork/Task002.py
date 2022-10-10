# Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.


import math


# метод для запроса у пользователя чисел с проверкой на условия
def input_int():
    try:
        num = int(input(f"Введите число для разложения на простые множители: "))
        return num if num > 1 else \
            quit('Ошибка. Введите целое число больше 1.')
    except ValueError:
        quit('Ошибка. Введите целое число больше 1.')


# метод для разложения введенного числа на простые множители
def prime_factors(input_num):
    prime_factors_list = []
    # проходим по всем числам от 2 до введенного
    for i in range(2, input_num + 1):
        # пока полученное число делится на текущее значение i без остатка, записываем этот делитель в список
        while not input_num % i:
            prime_factors_list.append(i)
            input_num //= i
    return prime_factors_list


# метод для вывода результатов пользователю
def main(input_list):
    print('\n' + '{} = {}' .format(math.prod(input_list), ' * '.join(map(str, input_list))))


main(prime_factors(input_int()))
