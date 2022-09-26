import random


def count(first_string, second_string):
    count = 0
    i = -1
    while True:
        i = first_string.find(second_string, i + 1)
        if i == -1:
            return count
        count += 1


# first_string = input('Введите первую строку: ')
# second_string = input('Введите вторую строку: ')


def random_string(num):
    string = ""
    for i in range(num):
        string += chr(random.randint(1070, 1100))
    print(string)
    return string

first_string = random_string(int(input('Введите количество символов первой строки: ')))
second_string = random_string(int(input('Введите количество символов второй строки: ')))
print(f"Количество вхождений второй строки в первую = {count(first_string, second_string)}")
print(f"Количество вхождений второй строки в первую = {first_string.count(second_string)}")
# random_string(50)