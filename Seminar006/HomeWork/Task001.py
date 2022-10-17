# Вывести на экран числа от -N до N.


# метод для запроса у пользователя чисел с проверкой на условия
def input_int():
    try:
        num = int(input(f"Введите число для построения последовательности: "))
        return num if num > 0 else \
            quit('Ошибка. Введите целое число больше 0.')
    except ValueError:
        quit('Ошибка. Введите целое число больше 0.')


num = input_int()
print(*[element for element in range(-num, num + 1)], sep=', ')
