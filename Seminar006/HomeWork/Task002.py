# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.


list_nums = [int(element) for element in input("Введите элементы списка через пробелы: ").split(' ') if element.isnumeric()]
sum_nums = sum(filter(lambda x: list_nums.index(x) % 2 != 0, list_nums))


print('Список элементов => ', list_nums, '\n', 'Сумма элементов на нечетных позициях = ', sum_nums)