# метод для запроса у пользователя целых чисел с проверкой на целочисленность
def input_int():
    try:
        num = int(input(f"Введите число: "))
        return int(num)
    except ValueError:
        quit(print('Ошибка. Вы ввели не целое число.'))

# метод для получения произведения чисел от 1 до введенного
def product_of_numbers(number):
    return number if number == 1 else number * product_of_numbers(number-1)


# метод для получения набор произведений чисел от 1 до N
def set_of_products_numbers(input_number):
    set_numbers = []
    for number in range(input_number):
        set_numbers.append(product_of_numbers(number + 1))
    return set_numbers


print(set_of_products_numbers(input_int()))