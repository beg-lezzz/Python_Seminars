# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

input_list = [int(element) for element in input("Введите элементы списка через пробелы: ").split(' ')
              if element.isnumeric()]

not_double = list(filter(lambda a: input_list.count(a) < 2, input_list))

print(not_double)
