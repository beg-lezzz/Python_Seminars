#метод для запроса у пользователя целых чисел с проверкой на целочисленность
def input_int(order):
    try:
        num = int(input(f"Введите координату {order}: "))
        return int(num) if int(num) != 0 else quit(print('Ошибка. Координата не может быть = 0'))
    except ValueError:
        quit(print('Ошибка. Вы ввели не целое число.'))


# метод для определения положения точки по четвертям координатной плоскости
def find_quarter(x, y):
    return "1 четверть" if x > 0 & y > 0 else \
        "2 четверть" if x < 0 & y > 0 else \
        "3 четверть" if x < 0 & y < 0 else \
        "4 четверть" if x > 0 & y < 0 else \
        "На пересечении осей"


coord_x = input_int("X")
coord_y = input_int("Y")
print(f"Расположение точки ({coord_x}, {coord_y}) - {find_quarter(coord_x, coord_y)}")
