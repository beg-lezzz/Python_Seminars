# метод для запроса у пользователя целых чисел с проверкой на целочисленность
def input_int():
    try:
        num = int(input(f"Введите число: "))
        return int(num)
    except ValueError:
        quit(print('Ошибка. Вы ввели не целое число.'))


# метод для проверки выполнения условия
def check_condition(num):
    if ((num % 5 == 0 and num % 10 == 0) or num % 15 == 0) and num % 30 != 0:
        print('Условие выполняется')
    else:
        print('Условие не выполняется')


check_condition(input_int())
