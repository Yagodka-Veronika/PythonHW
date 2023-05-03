# Задача 18:
# Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5
import random

n = int(input("Введите длину списка "))
array = []
for i in range(n):
    array.append(random.randint(-n, n + n // 2))

print(array)

x = int(input("Введите число "))
number = array[0]
max_number = abs(x - array[0])
for i in array:
    t = abs(x - i)
    if t < max_number:
        max_number = t
        number = i

print(f"-> {number}")

