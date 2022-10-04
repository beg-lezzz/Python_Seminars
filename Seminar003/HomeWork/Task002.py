#метод для ввода элементов списка через пробел
def input_list():
    return input("Введите элементы списка через пробелы: ").split(' ')


#метод для проверки списка на то, что в нм содержатся только числа
def check_list(input_list):
    for i in input_list:
        if not i.isnumeric():
            return False
        else:
            return True


#метод для нахождения произведения пар чисел списка (Парой считаем первый и последний элемент,
#второй и предпоследний и т.д.)
def pares_product(input_list):
    prod_list = []
    if check_list(input_list):
        for i in range(0, len(input_list) // 2):
            prod_list.append(int(input_list[i]) * int(input_list[len(input_list) - 1 - i]))
        if len(input_list) % 2 != 0:
            prod_list.append(int(input_list[len(input_list) // 2])**2)
    return prod_list


print(pares_product(input_list()))