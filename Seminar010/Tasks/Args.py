def my_func(x, y, *args):
    print(f'{x = }')
    print(f'{y = }')
    other = args
    print(f'{other = }')


my_func(5, 4, 15, 35, 12)

def my_func2(x, y, *, a, b, c):
    print(f'{x = }')
    print(f'{y = }')
    print(f'{a = }')
    print(f'{b = }')
    print(f'{c = }')


my_func2(5, 4, a=15, b=35, c=12)


def my_func3(*args, **kwargs):
    a, b, *c = args
    d = kwargs
    print(f'{a = }')
    print(f'{b = }')
    print(f'{c = }')
    print(f'{d = }')


my_func3(5, 4, 35, 'bnj', a=15, b=35, c=12)
