# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите число n "))
count0 = 0
count1 = 0
for i in range(1, n+1):
    a = int(input(f'Введите 0 или 1 в зависимости от того что выпало в {i} случае: '))
    if a == 1:
        count1 = count1 + 1
    elif a == 0:
         count0 = count0 + 1

if count1 < count0:
    print(count1)
else: 
    print(count0)