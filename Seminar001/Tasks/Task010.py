#метод для запроса у пользователя целых чисел с проверкой на целочисленность
def input_int(coord_name):
    try:
        num = int(input(f"Введите координату {coord_name}: "))
        return int(num)
    except ValueError:
        quit(print('Ошибка. Вы ввели не целое число.'))


# метод для заполнения массива целыми числами через запрос у пользователя ввести их с клавиатуры
def list_insert(point_name):
    counter = 0
    list = ["X", "Y"]
    list_coord = []
    print(f"Введите координаты точки {point_name} ")
    while counter < len(list):
        list_coord.insert(counter, input_int(list[counter]))
        counter += 1
    print()
    return list_coord


# метод для вычисления расстояние между точками в 2D пространстве
def point_distance(point_a, point_b):
    points_distance = ((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2) ** 0.5
    return round(points_distance, 2)


point_A = list_insert("A")
point_B = list_insert("B")
print(f"Расстояние между точкой А ({point_A[0]}, {point_A[1]}) и точкой B ({point_B[0]}, {point_B[1]}) "
      f"= {point_distance(point_A, point_B)}")