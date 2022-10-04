#метод для ввода элементов списка через пробел
def input_list():
    return input("Введите элементы списка через пробелы: ").split(' ')


#метод для проверки списка на то, что в нм содержатся только числа
def check_list(input_list):
    for i in input_list:
        try:
            float(i.replace(',', '.'))
            return True
        except ValueError:
            return False


#метод для формирования списка элементов - дробных частей введенных вещественных чисел
def fractional_part_list(input_list):
    fractional_list = []
    if check_list(input_list):
        for i in input_list:
            if float(i.replace(',', '.')) - int(float(i.replace(',', '.'))) > 0:
                fractional_list.append(round(float(i.replace(',', '.')) - int(float(i.replace(',', '.'))), 2))

    return fractional_list


#метод для нахождения разницы между максимальным и минимальным значением в списке (свой)
def diff_list_my(input_list):
    if len(input_list) > 0:
        min_num = float(input_list[0])
        max_num = float(input_list[0])
        for i in input_list:
            if float(i) < min_num:
                min_num = float(i)
            else:
                max_num = float(i)
        return max_num - min_num
    else:
        return '0. Список пуст.'


#метод для нахождения разницы между максимальным и минимальным значением в списке (встроенный)
def diff_list(input_list):
    return max(input_list) - min(input_list) if len(input_list) > 0 else '0. Список пуст.'


frac_list = fractional_part_list(input_list())
print(f'Разница между миниимум и максимум = {diff_list(frac_list)} (встроенные методы)')
print(f'Разница между миниимум и максимум = {diff_list_my(frac_list)} (свои методы)')
