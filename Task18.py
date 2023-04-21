# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
n = int(input('Введите количество элементов в массиве N: '))
x = int(input('Введите число X, близжайшее к которому мы будем искать: '))
list = []

for _ in range (n):
    list.append(random.randint(0, 20))
print(list)
print(x)

min = abs(x - list[0])
index = 0
for i in range(1, n):
        count = abs(x - list[i])
        if count < min:
            min = count
            index = i
print(f'Числe {x} в списке наиболее близко по величине число {list[index]}, и их разница составляет {abs(x - list[index])}')