import sqlite3

bd = sqlite3.connect('data_base.db')

cursor = bd.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS personal(
               id INTEGER PRIMARY KEY,
               name TEXT,
               last_name TEXT,
               position TEXT,
               slary INT,
               bonus INT)''')

to_base = [('Иван', 'Иванов', 'главный инженер', 50000, 10000),
           ('Петр', 'Петров', 'инженер', 20000, 8000),
           ('Семен', 'Семенов', 'завхоз', 12000, 3000)
           ]

# cursor.executemany('INSERT INTO personal(name,last_name,position,slary,bonus) VALUES(?,?,?,?,?)', to_base)
# bd.commit()

for i in cursor.execute('SELECT * FROM personal'):
    print(*i)

cursor.execute('select * from personal where name like "Иван";')
one = cursor.fetchone()
print(*one)

# cursor.execute('delete from personal where id=1')
# bd.commit()
#
# for i in cursor.execute('SELECT * FROM personal'):
#     print(*i)

# print(*list(cursor.execute('select * from personal where name like "Иван";')),sep='\n')
def preview_base():
    pass


def input_choice():
    while True:
        user_choice = input('1 - просмотреть всю базу\n2 - добавить запись\n3 - удалить запись\n4 - найти по ФИО'
                            '\nq - выход\n\nВведите свой выбор:')