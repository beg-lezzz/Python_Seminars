# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


# метод для сжатия строки алгоритмом RLE
def rle_code(input_string):
    rle_list = []
    count = 1
    for i in range(len(input_string)-1):
        if i <= len(input_string):
            if input_string[i] == input_string[i + 1]:
                count += 1
            else:
                rle_list.append(str(count) + input_string[i])
                count = 1
    rle_list.append(str(count) + input_string[i + 1])
    rle_string = ''.join(rle_list)

    return rle_string


# метод для восстановления строки, сжатой алгоритмом RLE
def rle_decode(input_string):
    decode_count = ''
    decode_string = ''
    for i in range(len(input_string)):
        if input_string[i].isdigit():
            decode_count += str(input_string[i])
        else:
            decode_string = decode_string + str(input_string[i]) * int(decode_count)
            decode_count = ''
    return decode_string


# основной метод для запуска остальных и вывода результатов пользователю
def main():
    input_string = input("Введите строку для RLE-кодировки: ")
    code = rle_code(input_string)
    decode = rle_decode(code)
    print('\n' + '*' * 15 + ' Первоначальная строка ' + '*' * 15 + '\n' + input_string + '\n' * 2 + '*' * 15 + ' Строка после сжатия (RLE) ' + '*' * 15 + '\n' + code +
          '\n' * 2 + '*' * 15 + ' Строка после восстановления ' + '*' * 15 + '\n' + decode)


main()
