# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

a = int(input("Введите натуральное число a: "))
b = int(input("Введите натуральное число b: "))
def summ(a, b):
    if b == 0:
        return a
    return summ(a + 1, b - 1)


print(summ(a, b))
