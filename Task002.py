a1 = int(input('Введите первое число: '))
a2 = int(input('Введите второе число: '))
a3 = int(input('Введите третье число: '))
a4 = int(input('Введите четвертое число: '))
a5 = int(input('Введите пятое число: '))

list = [a1, a2, a3, a4, a5]
i=0

while i<len(list)-1:
    if list[i] > list[i+1]:
        max = list[i]
        i = i + 1
    else:
        max = list[i+1]
        i = i + 1


print('Максимальное число = ', max)