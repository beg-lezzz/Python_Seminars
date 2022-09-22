count = 0
list=[]
while count < 5:
    list.insert(count, int(input('Введите число: ')))
    count +=1

i = 1
max = list[0]

while i < len(list):
    if list[i] > max:
        max = list[i]
    i += 1

print('Максимальное число = ', max)