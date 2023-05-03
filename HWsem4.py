# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
# возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.


def task22 ():

    import random
    n = int(input("Введите количество элементов первого множества "))
    m = int(input("Введите количество элементов второго множества "))

    one_set = set()
    two_set = set()
    for i in range(n):
        # one_set.add(random.randint(-n, n + n // 2))
        one_set.add(int(input("Введите элемент первого множества ")))

    for i in range(m):
        # two_set.add(random.randint(-m, m + m // 2))
        two_set.add(int(input("Введите элемент второго множества ")))

    print(one_set)
    print(two_set)
    arr_temp = []

    for i in one_set:
        for j in two_set:
            if i == j:
                arr_temp.append(i)
                break

    arr_temp.sort()

    print(arr_temp)



    # Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом
# кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля
# и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.'

def task24 ():

    import random

    n = int(input("Введите количесвто кустов"))

    arr_bush = []
    for i in range(n):
        # arr_bush.append(random.randint(1, n*2))
        arr_bush.append(int(input("Введите значение")))
    temp_val = "Длина листа короче шага"
    print(arr_bush)
    step = 3
    if len(arr_bush) > step:
        val = temp_val = sum(arr_bush[:step])

        for i in range(n-1):
            j = (i + step) % n
            val = val - arr_bush[i] + arr_bush[j]

            if val > temp_val:
                temp_val = val

    elif len(arr_bush) == step:
        temp_val = sum(arr_bush[:step])

    print(temp_val)
