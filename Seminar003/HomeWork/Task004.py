# метод для запроса у пользователя целых чисел с проверкой на целочисленность
def input_int():
    try:
        num = int(input(f"Введите число: "))
        return int(num) if int(num) >= 0 else quit(print('Ошибка. Введите целое число больше нуля.'))
    except ValueError:
        quit(print('Ошибка. Вы ввели не целое число.'))


#метод для преобразования десятичного числа в двоичное
def from_10_to_2(input_number):
    list_binary = []
    if input_number == 0:
        print(0)
    elif input_number == 1:
        print(1)
    else:
        while input_number > 0:
            list_binary.insert(0, input_number % 2)
            input_number = input_number // 2

        print(*list_binary, sep='')


from_10_to_2(input_int())
