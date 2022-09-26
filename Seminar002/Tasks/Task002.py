# метод для запроса у пользователя целых чисел с проверкой на целочисленность
def input_int():
    try:
        num = int(input(f"Введите число: "))
        return int(num) if int(num) > 0 else quit(print('Ошибка. Введите число больше нуля.'))
    except ValueError:
        quit(print('Ошибка. Вы ввели не целое число.'))


# метод для заполнения списка длины N (от 1 до N), где элемент = 3 * N + 1
def fill_list(input_number):
    list = []
    i = 1
    # в зависимости от знака введенного числа запускаем цикл либо на увеличение, либо на уменьшение
    while i <= input_number:
        list.insert(i - 1, i * 3 + 1)
        i += 1
    return list


print(*fill_list(input_int()), sep = ', ')
