# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# абв ваб абвг габа габв

input_string = input("Введите строку, из которой необходимо удалить слова: ")
find_string = input("Введите строку, слова содержащие которую, необходимо удалить: ")


print(f"Строка, из которой удалены все слова, содержащие '{find_string}' => "
      f"{' '.join(list(filter(lambda x: find_string not in x, input_string.split(' '))))}")


print(f"Слова, удаленные из строки => "
      f"{' '.join(list(filter(lambda x: find_string in x, input_string.split(' '))))}")