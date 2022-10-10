b = '1x^5 + 2x^4 + 2x^3 + 1x^2 + 3x + 1 = 0'
a = '2x^4 + 2x^3 + 9x^2 + 2x = 0'


# метод для чтения строк из файла и заполнения списка
def read_from_file():
    with open("polynominal.txt", "r") as file_with_poly:
        poly_list = file_with_poly.read().splitlines()
    file_with_poly.close()

    return poly_list


# метод для разбиения каждого многочлена на составляющие в формает словаря {множитель : степень}
def dict_from_polynomial(input_string):
    sum_list = {}
    input_list = input_string.split(' = ')[0].split(' + ')
    for i in input_list:
        if i.count('x^') > 0:
            try:
                sum_list[int(i.split('x^')[1])] = int(i.split('x^')[0])
            except ValueError:
                sum_list[int(i.split('x^')[1])] = 1
        elif i.count('x') > 0:
            try:
                sum_list[1] = int(i.split('x')[0])
            except ValueError:
                sum_list[1] = 1
        else:
            sum_list[0] = int(i)

    return sum_list


# метод для "сборки" списка словарей для дальнейшей обработки
def fill_list_of_polynominals(input_list):
    poly_list = []
    for i in input_list:
        poly_list.append(dict_from_polynomial(i))

    return poly_list


# метод для суммирования элементов словарей с одинаковыми ключами
def sum_of_dict(input_list):
    result_dict = {}
    for dict in input_list:
        for i in dict:
            try:
                result_dict[i] += dict[i]
            except KeyError:
                result_dict[i] = dict[i]

    return sorted(result_dict.items())


# метод для "сборки" многочлена из результирующего словаря
def fill_polynomial(input_list):
    sum_list = []
    for i in input_list:
        if i[0] == 0:
            sum_list.insert(0, str(i[1]))
        elif i[0] == 1:
            sum_list.insert(0, str(i[1]) + 'x') if i[1] != 1 else sum_list.insert(0, 'x')
        else:
            sum_list.insert(0, str(i[1]) + 'x^' + str(i[0])) if i[1] != 1 else sum_list.insert(0, 'x^' + str(i[0]))

    # return sum_list
    return " + ".join(sum_list) + ' = 0'


# метод для вывода результатов пользователю
def main(input_list):
    print('*' * 15 + ' Многочлены из файла для суммирования ' + '*' * 15)
    for i in input_list:
        print(i)
    print(f"\n{'*' * 15} Сумма многочленов {'*' * 15}\n{fill_polynomial(sum_of_dict(fill_list_of_polynominals(input_list)))}")


main(read_from_file())
