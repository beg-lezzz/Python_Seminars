# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


input_list = [int(element) for element in input("Введите элементы списка через пробелы: ").split(' ')
              if element.isnumeric()]

len_list = len(input_list) // 2 if len(input_list) % 2 == 0 else len(input_list) // 2 + 1

left_list = [element for element in input_list if input_list.index(element) + 1 <= len_list]
right_list = [element for element in input_list if input_list.index(element) + 1 >= len_list]
right_list.reverse()

print(*[x * y for x, y in zip(left_list, right_list)], sep=', ')
