# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1
import random

n = int(input("Введите длину списка "))
array = []
for i in range(n):
    array.append(random.randint(-n, n + n // 2))

print(array)
x = int(input("Введите искомое число "))
count = 0
for i in array:
    if i == x:
        count += 1

print(f"-> {count}")
