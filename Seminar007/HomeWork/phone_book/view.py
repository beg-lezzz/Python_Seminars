def view_data(title, data):
    print(f'{title} = {data}')


def get_value(nums_type):
    return int(input('value = ')) if nums_type == 1 else complex(input('value = '))


def get_operation():
    return input('operation = ')


def get_type():
    return int(input('Введите тип чисел для работы (1 - целые, 2 - комплексные) = '))
