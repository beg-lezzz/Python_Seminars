from scipy.optimize import fsolve
from sympy import symbols, sin, cos
from sympy.plotting import plot
import numpy


left_limit = -100
right_limit = 100


def print_func():
     x = symbols('x')
     plot(-12 * x ** 4 * sin(cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30,
          (x, left_limit, right_limit))


def f(x):
    return -12 * x ** 4 * numpy.sin(
        numpy.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30


def func_roots():
    global left_limit, right_limit
    tmp = left_limit
    right_limit = right_limit
    roots = []

    while tmp < right_limit:
        if (f(tmp) >= 0 and f(tmp + 1) <= 0) or (f(tmp) <= 0 and f(tmp + 1) >= 0):
            w = fsolve(f, tmp)
            roots.append(*w)
        tmp += 1
    roots = [round(i, 2) for i in roots]
    print(f'Корни для интервала ({tmp}, {right_limit}): {roots}')
    return roots


def func_interval(left, right):
    array = []
    temp = left
    while left <= right:
        array.append([round(f(left), 2), left])
        left += 0.1
    if array[0][0] > 0:
        print(f'f > 0 в промежутке {temp, right}')
        return max(array)
    else:
        print(f'f < 0 в промежутке {temp, right}')
        return min(array)


def main():
    roots = func_roots()

    if len(roots) < 2:
        print('На заданном интервале нет вершин')
    else:
        top = []
        for i in range(len(roots) - 1):
            top.append(func_interval(roots[i], roots[i + 1]))
        print(f'Координаты вершин: {top}')
        if len(top) < 2:
            print('Нет вершин')
        else:
            for i in range(len(top) - 1):
                if top[i][0] > top[i + 1][0]:
                    print(f'На промежутке ({round(top[i][1], 2)}, {round(top[i + 1][1], 2)}) Функция убывает')
                else:
                    print(f'На промежутке ({round(top[i][1], 2)}, {round(top[i + 1][1], 2)}) Функция возрастает')


if __name__ == '__main__':
    main()
    print_func()
