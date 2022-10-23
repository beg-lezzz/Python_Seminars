import sqlite3


def create_db():
    db = sqlite3.connect('employee_base.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employers(
                   id INTEGER PRIMARY KEY,
                   surname TEXT,
                   name TEXT,
                   patronymic TEXT,
                   position TEXT,
                   slary INT,
                   bonus INT)''')
    return db, cursor


def connect_db():
    db = sqlite3.connect('employee_base.db')
    cursor = db.cursor()
    return db, cursor
