# Задайте строку из набора чисел. Напишите программу, которая покажет большее и
# меньшее число. В качестве символа-разделителя используйте пробел.

# метод для создания списка, введенного пользователем
def input_list():
    return input("Введите элементы списка через пробелы: ").split(' ')


#метод для проверки списка на то, что в нм содержатся только целые
def check_list(input_list):
    flag = 0
    for i in input_list:
        try:
            int(i.replace('.', '').replace(',', ''))
        except ValueError:
            flag += 1
    return flag


def min_max(input_list):
    if check_list(input_list) == 0:
        return f"Минимум = {min(input_list)}, максимум = {max(input_list)}"
    else:
        return "Не все введенные элементы являются числами, либо список пуст"


print(min_max(input_list()))
