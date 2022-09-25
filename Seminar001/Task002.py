# метод для запроса у пользователя целых чисел с проверкой на целочисленность
def input_int(order):
    try:
        a = int(input(f"Введите {order}-е число: "))
        return int(a)
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


# метод для поиска максимального числа во входном массиве
def find_max(list):
    i = 1
    max = list[0]

    while i < len(list):
        if list[i] > max:
            max = list[i]
        i += 1
    return max


digits_amount = 5
print('Максимальное число = ', find_max(list_insert(digits_amount)))