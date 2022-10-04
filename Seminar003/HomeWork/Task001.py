def input_list():
    return input("Введите элементы списка через пробелы: ").split(' ')


#метод для проверки списка на то, что в нм содержатся только числа
def check_list(input_list):
    for i in input_list:
        if not i.isnumeric():
            return False
        else:
            return True


#метод для нахождения суммы элементов списка, стоящих на нечётной позиции
def odd_index_product(input_list):
    if check_list(input_list):
        if len(input_list) > 2:
            product_nums = 1
            for i in range(1, len(input_list), 2):
                product_nums *= int(input_list[i])
            return 'Произведение элементов на нечетных позициях = ' + str(product_nums)
        else:
            return 'Нет элементов на нечетных позициях'
    else:
        return 'В списке содержатся не только числа, либо список пуст'


print(odd_index_product(input_list()))