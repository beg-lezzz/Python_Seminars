# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.


import random


# метод для запроса у пользователя чисел с проверкой на условия
def input_int():
    try:
        num = int(input(f"Введите число элементов списка: "))
        return num if num > 1 else \
            quit('Ошибка. Введите целое число больше 1.')
    except ValueError:
        quit('Ошибка. Введите целое число больше 1.')


# метод для заполнения списка случайными числами в количестве, введенном пользователем
def fill_list_rnd(input_num):
    input_list = []
    for i in range(input_num):
        input_list.append(random.randint(0, 10))
    return input_list


# метод для создания списка из элементов исходного списка, которые не повторяются
def exclude_duplicates(input_list):
    type(input_list)
    new_list = []
    for i in input_list:
        if input_list.count(i) < 2:
            new_list.append(i)
    return input_list, new_list


# метод для вывода результата пользователю
def main(input_list):
    print('\n' + '*' * 15 + ' Исходный список ' + '*' * 15 + '\n' + ', '.join(str(x) for x in input_list[0]) + '\n' * 2
          + '*' * 15 + ' Список неповторяющихся ' + '*' * 15 + '\n'  + ', '.join(str(x) for x in sorted(input_list[1])) + '\n' * 2
          + '*' * 15 + ' Список уникальных ' + '*' * 15 + '\n'  + ', '.join(str(x) for x in sorted(set(input_list[0]))) + '\n')


main(exclude_duplicates(fill_list_rnd(input_int())))

