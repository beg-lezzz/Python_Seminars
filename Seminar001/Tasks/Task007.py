# метод для запроса у пользователя целых чисел с проверкой на целочисленность
def input_int(order):
    try:
        num = int(input(f"Введите {order}-е значение: "))
        return int(num) if int(num) in (0, 1) else quit(print('Ошибка. Вводить необходимо 0 или 1'))
    except ValueError:
        quit(print('Ошибка. Вы ввели не целое число.'))


# метод для заполнения массива целыми числами через запрос у пользователя ввести их с клавиатуры
def list_insert(dig_amount):
    counter = 0
    list = []
    while counter < dig_amount:
        list.insert(counter, input_int(counter + 1))
        counter +=1
    return list

# метод для проверки справедливочти двух утверждений
def check_condition(list):
    if not(list[0] or list[1] or list[2]) == (not(list[0]) and not(list[1]) and not(list[2])):
        print('Утверждение верно')
    else:
        print('Утверждение ложно')


digits_amount = 3
check_condition(list_insert(digits_amount))
