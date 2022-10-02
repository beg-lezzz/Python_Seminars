import math
# метод для запроса у пользователя целых чисел с проверкой на целочисленность
def input_int():
    try:
        num = int(input(f"Введите число: "))
        return int(num) if int(num) > 0 else quit(print('Ошибка. Введите целое число больше нуля.'))
    except ValueError:
        quit(print('Ошибка. Вы ввели не целое число.'))


# метод для заполнения списка значениями от -N до N
def fill_list(input_number):
    list_numbers = []
    i = -input_number
    while i <= input_number:
        list_numbers.append(i)
        i += 1
    return list_numbers


# метод для чтения строк из файла и заполнения списка
def read_from_file():
    set_positions = []
    with open("file.txt", "r") as file_with_positions:
        set_positions_temp = file_with_positions.read().splitlines()
    file_with_positions.close()
    # формируем новый список значений, удовлетворяющих условию - целое число от нуля
    for i in set_positions_temp:
        if i.isdigit() is True:
            set_positions.append(i)
    return set_positions


# метод для рассчета произведение чисел исходного списка на указанных позициях
def sum_numbers(input_list, list_with_positions):
    product_of_numbers = 1 if len(list_with_positions) > 0 and int(min(list_with_positions, key=lambda k: int(k))) < len(input_list) else 0
    for i in list_with_positions:
        if 0 <= int(i) < len(input_list):
            product_of_numbers *= int(input_list[int(i)])
    return product_of_numbers


# основной метод, вызывающий необходимые рабочие методы и производящий вывод
def main():
    num_set = fill_list(input_int())
    positions_set = read_from_file()
    print(f"Исходный список от {num_set[0]} до {num_set[-1]}: \n{num_set}")
    print(f"Список с позициями суммирования из файла: \n{positions_set}")
    print(f"Произведение чисел исходного списка на указанных позициях = {sum_numbers(num_set, positions_set)}")


main()
