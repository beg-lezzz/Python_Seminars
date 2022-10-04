def input_list():
    return input("Введите элементы списка через пробелы: ").split(' ')


def find_digits(input_list, digit):
    for i in input_list:
        if digit in i:
            print(f"В списке есть элемент, содержащи число {digit} => {i} (индекс = {input_list.index(i)})")


find_digits(input_list(), input("Введите число для поиска: "))