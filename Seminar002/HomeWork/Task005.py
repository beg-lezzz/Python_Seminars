#метод для получения списка из файла
def read_from_file():
    with open("file.txt", "r") as file_with_positions:
        set_positions = file_with_positions.read().splitlines()
    file_with_positions.close()
    return set_positions


# метод для перемешивания списка - меняем местами элементы на четных позициях с элементами на нечетных
def shuffle_set(input_list):
    for i in range(0, len(input_list), 2):
        if i + 1 < len(input_list):
            tmp = input_list[i]
            input_list[i] = input_list[i + 1]
            input_list[i + 1] = tmp
    return input_list


print(read_from_file())
print(shuffle_set(read_from_file()))