from datetime import datetime
import time
import sqlite3
import settings

db = sqlite3.connect('employee_base.db')
cursor = db.cursor()

def del_record(choice):
    if choice == '3-0':
        return '0-2'
    else:
        find_records(choice)
        del_positions = input('Введите номер(а) записи(ей) для удаления через пробел: ').split(' ')
        for_del = list(map(lambda x: str(int(del_positions[del_positions.index(x)]) - 1), del_positions))
        with open('phonebook.txt', 'r', encoding='utf-8') as phonebook:
            all_line = phonebook.read().splitlines(True)
        phonebook.close()
        for index_del in for_del:
            for strings in all_line:
                if index_del == strings[0]:
                    all_line.remove(strings)
        for strings in all_line:
            all_line[all_line.index(strings)] = str(all_line.index(strings)) + strings[1:]
        with open('phonebook.txt', 'w', encoding='utf-8') as phonebook:
            phonebook.writelines(all_line)

        print("\n\033[32mЗапись успешно удалена.\033[0m")
        time.sleep(1)
        return '0-2'


def add_record():
    question = ['Фамилия: ', 'Имя: ', 'Отчество: ', 'Должность: ', 'Заработная плата, руб.: ', 'Премия, руб.:']
    new_string = []
    for quest in question:
        input_string = input(quest)
        while True:
            if (quest == question[4] or quest == question[5]) and not input_string.isdigit():
                print('\033[31mНеобходимо вводить только целые числа при заполнении зарплаты и премии.\033[0m')
                input_string = input(quest)
            elif input_string != '':
                new_string.append(int(input_string)) if quest == question[4] or quest == question[5] \
                    else new_string.append(input_string)
                break
            else:
                print('\033[31mСтрока не должна быть пустой. Повторите ввод.\033[0m')
                input_string = input(quest)

    if not new_string == []:
        cursor.executemany('INSERT INTO employers(surname,name,patronymic,position,slary,bonus) VALUES(?,?,?,?,?,?)',
                           (new_string,))
        db.commit()
        print("\n\033[32mЗапись успешно добавлена\033[0m")

    time.sleep(1)
    return ('0-2')


def find_records(choice):
    with open('phonebook.txt', 'r+', encoding='utf-8') as phonebook:
        dict_lines = {elem.split(';')[0]: elem.split(';')[1:] for elem in phonebook.read().splitlines()}
    phonebook.close()
    if choice == '3-1':
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
    else:
        input_string = input('Введите телефон в формате 9ХХХХХХХХХ: ')
        while True:
            if input_string != '' and len(input_string) == 10:
                find_results = dict(filter(lambda item: ' '.join(item[1]).count(input_string) > 0, dict_lines.items()))
                break
            else:
                print('\033[31mОшибка. Повторите ввод.\033[0m')
                input_string = input('Введите телефон в формате 9ХХХХХХХХХ: ')
    if find_results != {}:
        print(f'\n\033[32mНайдено записей => {len(find_results)}.\033[0m')
        print('\n\033[32mНачало вывода результатов поиска.\033[0m')
        for k in find_results:
            print('\n' + '*' * 15 + ' Запись №' + str(int(k) + 1) + ' ' + '*' * 15)
            print(*find_results[k], sep=' ')
        print('\n\033[32mВывод результатов поиска завершен.\033[0m')
    else:
        print('\n\033[32mПо заданным параметрам ничего не найдено.\033[0m')

    return ('0-3', find_results)


def export_phonebook(choice):
    with open('phonebook.txt', 'r', encoding='utf-8') as phonebook:
        all_line = phonebook.read().splitlines(True)
    phonebook.close()
    if choice == '4-2':
        with open(f"export/csv/export_phonebook_{datetime.now().strftime('%d%m%y%H%M%S')}.csv",
                  'w+', encoding='cp1251') as phonebook:
            phonebook.writelines(all_line)
        file_format = 'csv'
    elif choice == '4-1':
        with open(f"export/txt/export_phonebook_{datetime.now().strftime('%d%m%y%H%M%S')}.txt",
                  'a+', encoding='utf-8') as phonebook:
            for lines in all_line:
                for fields in lines.split(';'):
                    phonebook.writelines(fields + '\n')
            phonebook.writelines('\n\n')
        file_format = 'txt'
    print(f'\n\033[32mСправочник успешно экспортирован в формат .{file_format}.\033[0m')
    time.sleep(1)

    return '0-4'

# ГОТОВО
def print_phonebook():
    # db = settings.connect_db()[0]
    cursor = settings.connect_db()[1]
    cursor.execute('SELECT * FROM employers')
    all_line = list(cursor.fetchall())

    if not all_line == []:
        print('\n\033[32mНачало вывода справочника.\033[0m')
        for record in all_line:
            print(*record)
        print('\n\033[32mВывод справочника завершен.\033[0m')
    else:
        print('\n\033[32mСправочник пока пуст. Вы можете добавить в него первую запись.\033[0m')
        time.sleep(1)

    return '0'


def import_phonebook(choice):
    if choice == '5-2':
        with open('import/csv/import_phonebook.csv', 'r', encoding='cp1251') as phonebook:
            all_line = phonebook.read().splitlines()
        with open('phonebook.txt', 'a+', encoding='utf-8') as phonebook:
            for x in all_line:
                phonebook.write("\n" + x)
            phonebook.close()
        with open('phonebook.txt', 'r+', encoding='utf-8') as phonebook:
            all_line = phonebook.read().splitlines(False)
            for i in range(len(all_line)):
                all_line[i] = str(i) + all_line[i][1:]
            phonebook.close()
        with open('phonebook.txt', 'w', encoding='utf-8') as phonebook:
            for x in all_line:
                if all_line.index(x) == 0:
                    delimetr = ''
                else:
                    delimetr = '\n'
                phonebook.write(delimetr + x)
        file_format = 'csv'
    elif choice == '5-1':
        with open('import/txt/import_phonebook.txt', 'r', encoding='utf-8') as phonebook:
            all_line = phonebook.read().splitlines()
            new_line = []
            string_new = ''
            for x in all_line:
                if x != '':
                    string_new += x + ';'
                else:
                    new_line.append(string_new[:-1])
                    string_new = ''
            phonebook.close()
        with open('phonebook.txt', 'a+', encoding='utf-8') as phonebook:
            for x in new_line:
                phonebook.write("\n" + x)
            phonebook.close()
        with open('phonebook.txt', 'r+', encoding='utf-8') as phonebook:
            all_line = phonebook.read().splitlines(False)
            for i in range(len(all_line)):
                all_line[i] = str(i) + all_line[i][1:]
            phonebook.close()
        with open('phonebook.txt', 'w', encoding='utf-8') as phonebook:
            for x in all_line:
                if all_line.index(x) == 0:
                    delimetr = ''
                else:
                    delimetr = '\n'
                phonebook.write(delimetr + x)
        file_format = 'txt'
    print(f'\n\033[32mСправочник успешно импортирован из формата .{file_format}.\033[0m')
    time.sleep(1)

    return '0-5'
