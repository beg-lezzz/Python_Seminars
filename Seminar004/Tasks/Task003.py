# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее
# кратное) этих двух чисел.

def input_nums():
    nums_list = []
    for i in (1, 2):
        nums_list.append(int(input(f"Введите {i}-е число: ")))
    return nums_list


def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)


def nok(input_list):
    a, b = input_list
    return int(abs(a * b) / nod(a, b))


print(f"Наименьшее общее кратное = {nok(input_nums())}")
