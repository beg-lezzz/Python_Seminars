# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

input_list = [int(element) for element in input("Введите элементы списка через пробелы: ").split(' ')
              if element.isnumeric()]

not_double = list(filter(lambda x: input_list.count(x) < 2, input_list))

print(not_double)
