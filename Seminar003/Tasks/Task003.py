def input_list():
    return input("Введите элементы списка через пробелы: ").split(' ')


def find_digits(input_list, digit):
    print(f"Позиция второго вхождения строки в списке => "
          f"{input_list.index(digit, input_list.index(digit) + 1) if input_list.count(digit) > 1 else 'Отсутствует'}")


find_digits(input_list(), input("Введите строку для поиска: "))