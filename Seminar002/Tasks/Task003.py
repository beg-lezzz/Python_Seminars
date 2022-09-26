def count(first_string, second_string):
    count = 0
    i = -1
    while True:
        i = first_string.find(second_string, i + 1)
        if i == -1:
            return count
        count+=1

first_string = input('Введите первую строку: ')
second_string = input('Введите вторую строку: ')

print(f"Количество вхождений второй строки в первую = {count(first_string, second_string)}")
print(f"Количество вхождений второй строки в первую = {first_string.count(second_string)}")
