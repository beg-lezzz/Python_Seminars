# метод для запроса у пользователя целых чисел с проверкой на целочисленность
def input_int():
    try:
        num = int(input(f"Введите число: "))
        return int(num) if int(num) >= 0 else quit(print('Ошибка. Введите целое число больше нуля.'))
    except ValueError:
        quit(print('Ошибка. Вы ввели не целое число.'))


#метод для расчета числа Фибоначчи
def negafib(num):
    if num == -1:
        return 1
    if num == -2:
        return -1
    else:
        return negafib(num + 2) - negafib(num + 1)


#метод для расчета числа негаФибоначчи
def fib(num):
    if num == 0:
        return 0
    if num in (1, 2):
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


#метод для формирования полного списка чисел Фибоначчи (и обычные и негв)
def all_fib(input_number):
    out_list = []
    for i in range(input_number + 1):
        if i == 0:
            out_list.append(fib(i))
        if i > 0:
            out_list.append(fib(i))
            out_list.insert(0, negafib(-i))
    return out_list


print(all_fib(input_int()))