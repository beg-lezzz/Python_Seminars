# Вывести на экран числа от -N до N.


# метод для запроса у пользователя чисел с проверкой на условия
def input_int():
    try:
        num = int(input(f"Введите число для разложения на простые множители: "))
        return num if num > 0 else \
            quit('Ошибка. Введите целое число больше 0.')
    except ValueError:
        quit('Ошибка. Введите целое число больше 0.')


num = input_int()
print(*[x for x in range(-num, num + 1)], sep=', ')
