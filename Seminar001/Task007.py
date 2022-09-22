x = input('Введите первое значение: ')
y = input('Введите второе значение: ')
z = input('Введите третье значение: ')

if not(x or y or z) == (not(x) and not(y) and not(z)):
    print('Утверждение верно')
else:
    print('Утверждение ложно')