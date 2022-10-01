# метод для запроса у пользователя целых чисел с проверкой на целочисленность
def input_int():
    try:
        num = int(input(f"Введите число: "))
        return int(num) if int(num) > 0 else quit(print('Ошибка. Введите целое число больше нуля.'))
    except ValueError:
        quit(print('Ошибка. Вы ввели не целое число.'))


# метод для задания списка из N чисел последовательности (1 + 1 / (N)) ** (N)
def set_of_numbers(number):
    number_list = []
    for i in range(number):
        number_list.append((1 + 1 / (i + 1)) ** (i + 1))

    return number_list


# рекурсивный метод для суммирования элементов списка из N элементов последовательности (1 + 1 / (N)) ** (N)
def sum_of_numbers(number):
    if number != 0:
        sum_numbers = ((1 + 1 / (number)) ** (number))
        return sum_numbers + sum_of_numbers(number - 1)
    else:
        return 0


input_number = input_int()
num_list = set_of_numbers(input_number)
print(f"\nПоследовательность чисел:\n{num_list}\nСумма чисел = {sum(num_list)} (цикл)\n"
      f"Сумма чисел = {sum_of_numbers(input_number)} (рекурсия)")
