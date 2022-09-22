a = int(input('Введите число: '))

list=[]
i = -a
len = 1
while i < a:
    list.insert(len, i)
    len+=1
    i+=1

print(list)
