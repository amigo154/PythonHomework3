# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

import random
n = int(input('Введите количество элементов в массиве N: '))
x = int(input('Введите число которое необходимо найти: '))
list = []

for _ in range (n):
    list.append(random.randint(0, 20))
print(list)
print(x)

Sum = 0
i = 0
while n > i:
    if list[i] == x:
        Sum += 1
    i += 1
print(f'Число X = {x} в данном массиве встречается {Sum} раз(a)')
