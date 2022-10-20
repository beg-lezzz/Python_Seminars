from datetime import datetime
import time


def del_record(x, y):
    return x * y


def add_record():
    question = ['Фамилия: ', 'Имя: ', 'Отчество: ', 'Телефон в формате 9ХХХХХХХХХ: ', 'Комментарий: ']
    new_string = []
    for quest in question:
        input_string = input(quest)
        while True:
            if quest == question[3] and len(input_string) != 10:
                print('\033[31mТелефон необходимо вводить в формате 9ХХХХХХХХХ. Повторите ввод.\033[0m')
                input_string = input(quest)
            elif input_string != '':
                new_string.append(input_string)
                break
            else:
                print('\033[31mСтрока не должна быть пустой. Повторите ввод.\033[0m')
                input_string = input(quest)
    with open('phonebook.txt', 'r+', encoding='utf-8') as phonebook:
        try:
            last_id = str(int(list(phonebook.read().splitlines()[-1].split(';'))[0]) + 1)
            line_break = '\n'
        except IndexError:
            last_id = '0'
            line_break = ''
        phonebook.write(line_break + last_id + ";" + ';'.join(new_string))
    print("\n\033[32mЗапись успешно добавлена\033[0m")
    time.sleep(1)
    return ('0-2')


def find_fio():
    with open('phonebook.txt', 'r+', encoding='utf-8') as phonebook:
        dict_lines = {elem.split(';')[0]: elem.split(';')[1:] for elem in phonebook.read().splitlines()}
    phonebook.close()
    question = ['Фамилия: ', 'Имя: ', 'Отчество: ']
    new_string = []
    for quest in question:
        input_string = input(quest)
        while True:
            if input_string != '':
                new_string.append(input_string)
                break
            else:
                print('\033[31mСтрока не должна быть пустой. Повторите ввод.\033[0m')
                input_string = input(quest)

    find_results = dict(filter(lambda item: ' '.join(item[1]).count(' '.join(new_string)) > 0, dict_lines.items()))
    if find_results != {}:
        print(f'\n\033[32mНайдено записей => {len(find_results)}.\033[0m')
        print('\n\033[32mНачало вывода результатов поиска.\033[0m')
        for k in find_results:
            print('\n' + '*' * 15 + ' Запись №' + str(int(k) + 1) + ' ' + '*' * 15)
            print(*find_results[k], sep=' ')
        print('\n\033[32mВывод результатов поиска завершен.\033[0m')
    else:
        print('\n\033[32mПо заданным параметрам ничего не найдено.\033[0m')

    return '0-3'


def find_number(x, y):
    return x / y


def import_phonebook(choice):
    with open('phonebook.txt', 'r', encoding='utf-8') as phonebook:
        all_line = phonebook.read().splitlines(True)
    phonebook.close()
    if choice == '4-2':
        with open(f"export/csv/import_phonebook_{datetime.now().strftime('%d%m%y%H%M%S')}.csv",
                  'w+', encoding='cp1251') as phonebook:
            phonebook.writelines(all_line)
        file_format = 'csv'
    elif choice == '4-1':
        with open(f"export/txt/import_phonebook_{datetime.now().strftime('%d%m%y%H%M%S')}.txt",
                  'a+', encoding='utf-8') as phonebook:
            for lines in all_line:
                for fields in lines.split(';'):
                    phonebook.writelines(fields + '\n')
            phonebook.writelines('\n\n')
        file_format = 'txt'
    print(f'\n\033[32mСправочник успешно импортирован в формат .{file_format}.\033[0m')
    time.sleep(1)

    return '0-4'


def print_phonebook():
    with open('phonebook.txt', 'r', encoding='utf-8') as phonebook:
        all_line = phonebook.read().splitlines()
    phonebook.close()
    if not all_line == []:
        print('\n\033[32mНачало вывода справочника.\033[0m')
        for record in all_line:
            print('\n' + '*' * 15 + ' Запись №' + str(int(list(record.split(';'))[0]) + 1) + ' ' + '*' * 15)
            print(*list(record.split(';'))[1:], sep=' ')
        print('\n\033[32mВывод справочника завершен.\033[0m')
    else:
        print('\n\033[32mСправочник пока пуст. Вы можете добавить в него первую запись.\033[0m')
        time.sleep(1)

    return '0'


# with open('phonebook.txt', 'r+', encoding='utf-8') as phonebook:
#     # dict_lines = {elem.split(';')[0]: ' '.join(elem.split(';')[1:]) for elem in phonebook.read().splitlines()}
#     dict_lines = {elem.split(';')[0]: elem.split(';')[1:] for elem in phonebook.read().splitlines()}
#     print(dict_lines)
#     question = ['Фамилия: ', 'Имя: ', 'Отчество: ']
#     new_string = []
#     for quest in question:
#         input_string = input(quest)
#         while True:
#             if input_string != '':
#                 new_string.append(input_string)
#                 break
#             else:
#                 print('\033[31mСтрока не должна быть пустой. Повторите ввод.\033[0m')
#                 input_string = input(quest)
#
#     find_results = dict(filter(lambda item: ' '.join(item[1]).count(' '.join(new_string)) > 0, dict_lines.items()))
#     print_list = []
#     for k in find_results:
#         print('\n' + '*' * 15 + ' Запись №' + str(int(k) + 1) + ' ' + '*' * 15)
#         print(*find_results[k], sep=' ')
#         a = list(find_results[k])
#         a.insert(0, k)
#         print_list.append(a)
#     print('\n\033[32mНачало вывода результатов поиска.\033[0m')
#     for record in print_list:
#         print('\n' + '*' * 15 + ' Запись №' + str(int(record[0]) + 1) + ' ' + '*' * 15)
#         print(*list(record)[1:], sep=' ')
#     print('\n\033[32mВывод результатов поиска завершен.\033[0m')
#
#     print(print_list)
#     # print(list(find_results[0:]))