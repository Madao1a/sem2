
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число n "))
a = int(0)
for i in range(0,n):
    a = int(2**i)
    if a<n:
        print(a)
    



# i = int(0)
# while a<n:
#     a = int(2**i)
#     if a<n:
#         print(a)
#     i = i+1
