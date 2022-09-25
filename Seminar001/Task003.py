# метод для запроса у пользователя целых чисел с проверкой на целочисленность
def input_int():
    try:
        num = int(input(f"Введите число: "))
        return int(num)
    except ValueError:
        quit(print('Ошибка. Вы ввели не целое число.'))


# метод для заполнения списка числами от -N до N
def fill_list(input_number):
    list = []
    i = -input_number
    len = 1
    # в зависимости от знака введенного числа запускаем цикл либо на увеличение, либо на уменьшение
    while i <= input_number if input_number > 0 else i >= input_number:
        list.insert(len, i)
        len += 1
        # в зависимости от знака введенного числа либо инкрементируем, либо декрементируем i
        if input_number > 0:
            i += 1
        else:
            i -= 1
    return list


print(fill_list(input_int()))
