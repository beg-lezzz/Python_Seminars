from datetime import datetime
import time
import settings

db = settings.connect_db()[0]
cursor = db.cursor()


def del_record(choice):
    if choice == '3-0':
        return '0-2'
    else:
        find_results = find_records(choice)
        find_positions = []
        if find_results[1] != ['']:
            for i in find_results[1]:
                find_positions.append(i[0])
            while True:
                del_positions = input('Введите номер(а) записи(ей) для удаления через пробел: ').split(' ')
                if del_positions == ['']:
                    print("\n\033[32mВы не ввели номера записей.\033[0m")
                else:
                    del_positions_string = ', '.join(del_positions)
                    del_positions = [int(i) for i in del_positions]
                    if set(del_positions).issubset(find_positions) and del_positions != ['']:
                        query = f"DELETE FROM employers WHERE id IN ({del_positions_string})"
                        cursor.execute(query)
                        db.commit()
                        print("\n\033[32mЗапись успешно удалена.\033[0m")
                        break
                    else:
                        print("\n\033[32mВы ввели номера записей не из результатов поиска.\033[0m")
                        continue
        time.sleep(1)

    return '0-2'


def edit_record(choice):
    if choice == '3-0':
        return '0-2'
    else:
        find_results = find_records(choice)
        find_positions = []
        if find_results[1] != ['']:
            for i in find_results[1]:
                find_positions.append(i[0])
            while True:
                edit_position = input('Введите номер записи для корректировки зарплаты и премии: ')
                if edit_position == '':
                    print("\n\033[32mВы не ввели номера записей.\033[0m")
                else:
                    edit_list = [int(i) for i in edit_position]
                    if set(edit_list).issubset(find_positions) and edit_list != ['']:
                        question = ['Заработная плата: ', 'Премия: ']
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
                        query = f"UPDATE employers SET slary = {new_string[0]}, bonus = {new_string[1]} WHERE id = {int(edit_position)}"
                        cursor.execute(query)
                        db.commit()
                        print("\n\033[32mЗапись успешно обновлена.\033[0m")
                        break
                    else:
                        print("\n\033[32mВы ввели номера записей не из результатов поиска.\033[0m")
        else:
            return '2-2'
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

        cursor.execute(f"select * from employers where (surname || ' ' || name || ' ' || patronymic) "
                       f"like '{' '.join(new_string)}'")
        find_results = list(cursor.fetchall())
    if find_results != []:
        print(f'\n\033[32mНайдено записей => {len(find_results)}.\033[0m')
        print('\n\033[32mНачало вывода результатов поиска.\033[0m')
        for record in find_results:
            print('\n' + '*' * 15 + ' Запись №' + str((record[0])) + ' ' + '*' * 15)
            print(*record[1:], sep=' ')
        print('\n\033[32mВывод результатов поиска завершен.\033[0m')
    else:
        print('\n\033[32mПо заданным параметрам ничего не найдено.\033[0m')

    return ('0-3', find_results)


def export_data_base(choice):
    cursor.execute('SELECT * FROM employers')
    all_line = list(cursor.fetchall())
    if choice == '4-2':
        with open(f"export/csv/export_data_base_{datetime.now().strftime('%d%m%y%H%M%S')}.csv",
                  'w+', encoding='cp1251') as phonebook:
            rec_string = ''
            for record in all_line:
                record = [str(i) for i in record]
                rec_string += ';'.join(record)
                rec_string += '\n'
            phonebook.writelines(rec_string)
            phonebook.close()
        file_format = 'csv'
    elif choice == '4-1':
        with open(f"export/txt/export_data_base_{datetime.now().strftime('%d%m%y%H%M%S')}.txt",
                  'a+', encoding='utf-8') as phonebook:
            rec_string = ''
            for record in all_line:
                record = [str(i) for i in record]
                rec_string += '\n'.join(record)
                rec_string += '\n\n'
            phonebook.writelines(rec_string)
            phonebook.close()
        file_format = 'txt'
    print(f'\n\033[32mБаза успешно экспортирована в формат .{file_format}.\033[0m')
    time.sleep(1)

    return '0-4'


def print_data_base():
    db = settings.connect_db()[0]
    cursor = settings.connect_db()[1]
    cursor.execute('SELECT * FROM employers')
    all_line = list(cursor.fetchall())

    if not all_line == []:
        print('\n\033[32mНачало вывода базы.\033[0m')
        test = {}
        for record in all_line:
            test[list(record)[0]] = list(record)[1:]
        for key, val in test.items():
            print('\n' + '*' * 15 + ' Запись №' + str(key) + ' ' + '*' * 15)
            print(*val)
        print('\n\033[32mВывод базы завершен.\033[0m')
    else:
        print('\n\033[32mБаза пока пуста. Вы можете добавить в нее первую запись.\033[0m')
        time.sleep(1)

    return '0'


def import_data_base(choice):
    if choice == '5-2':
        with open('import/csv/import_data_base.csv', 'r', encoding='cp1251') as phonebook:
            all_line = phonebook.read().splitlines()
            all_line = ([list(i.split(';'))[1:] for i in all_line])
        cursor.executemany('INSERT INTO employers(surname,name,patronymic,position,slary,bonus) VALUES(?,?,?,?,?,?)',
                           all_line)
        db.commit()
        file_format = 'csv'
    elif choice == '5-1':
        with open('import/txt/import_data_base.txt', 'r', encoding='utf-8') as phonebook:
            all_line = (phonebook.read().splitlines())
            query_line = []
            rec_string = ''
            for i in all_line:
                if i != '':
                    rec_string += i + ','
                else:
                    query_line.append(list((rec_string[0:-1]).split(',')[1:]))
                    rec_string = ''
        cursor.executemany('INSERT INTO employers(surname,name,patronymic,position,slary,bonus) VALUES(?,?,?,?,?,?)',
                           query_line)
        db.commit()
        file_format = 'csv'
    print(f'\n\033[32mСправочник успешно импортирован из формата .{file_format}.\033[0m')
    time.sleep(1)

    return '0-5'
