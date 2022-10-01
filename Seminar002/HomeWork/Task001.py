# метод для запроса у пользователя вещественных чисел с проверкой
def input_int():
    try:
        num = float(input("Введите вещественное число: "))
        return str(num).replace('.', '')
    except ValueError:
        quit(print('Ошибка. Вы ввели не вещественное число.'))


# метод для суммирования цифр в вещественном числе, введенном пользователем
def sum_digits_string(in_string):
    set_numbers = []
    sum_digits = 0
    minus_num = 0

    # проводим проверку на отрицательное число. если отрицательное, то записываем в переменную первое число с минусом
    if in_string[0] == '-':
        # умножаем на (-2), т.к. первое число войдет в сумму и его нужно будет вычесть дважды
        minus_num = int(in_string[1]) * -2
        in_string = in_string.replace('-', '')

    # суммируем все числа в исходной строке
    for i in in_string:
        sum_digits += int(i)
        set_numbers.append(i)

    # выводим полученную сумму с поправкой на
    return sum_digits + minus_num


print(sum_digits_string(input_int()))
