#метод для запроса у пользователя целых чисел с проверкой на целочисленность
def input_int(order):
    try:
        a = int(input(f"Введите {order} число: "))
        return int(a)
    except ValueError:
        print('Ошибка. Вы ввели не целое число.')

#метод для определения является ли число квадратом другого числа
def check_square(a,b):
   if a**2 == b:
       print('Второе квадрат первого')
   elif b**2 == a:
       print('Первое квадрат второго')
   else:
       print('Ни одно не является квадратом другого')

a = input_int("первое")
b = input_int("второе")

check_square(a,b)