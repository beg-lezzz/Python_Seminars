# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения;
# 2) с помощью дополнительных библиотек Python.
import math
def input_coefficients():
    coefficients_list = []
    for i in ('A', 'B', 'C'):
        coefficients_list.append(int(input(f"Введите коэффициент {i}: ")))
    return coefficients_list


def solution_equation(input_list):
    a, b, c = input_list
    d = b ** 2 - 4 * a * c
    if d == 0:
        x1 = round(-b / 2 * a, 2)
        return f"Уравнение имеет один корень = {x1}"
    elif d > 0:
        x1 = round((-b + d ** 0.5) / 2 * a, 2)
        x2 = round((-b - d ** 0.5) / 2 * a, 2)
        return f"Уравнение имеет два корня = {x1}, {x2}"
    else:
        return "Уравнение не имеет корней"


def solution_equation_lib(input_list):
    a, b, c = input_list
    d = b ** 2 - 4 * a * c
    if d == 0:
        x1 = round(-b / 2 * a, 2)
        return f"Уравнение имеет один корень = {x1}"
    elif d > 0:
        x1 = round((-b + math.sqrt(d)) / 2 * a, 2)
        x2 = round((-b - math.sqrt(d)) / 2 * a, 2)
        return f"Уравнение имеет два корня = {x1}, {x2}"
    else:
        return "Уравнение не имеет корней"


def main():
    coefficients_list = input_coefficients()
    print('\n' + '*' * 15 + ' Без библиотеки ' + '*' * 15 + '\n' + solution_equation(coefficients_list) + '\n' * 2
          + '*' * 15 + ' С библиотекой ' + '*' * 15 + '\n' + solution_equation(coefficients_list))


main()
