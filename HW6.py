# Задача 6:
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no


numberTicket = input("Введите номер билета ")
if numberTicket.isdigit() and len(numberTicket) > 5:
    
    numberFirst = int(numberTicket[:3])
    numberSecond = int(numberTicket[-3:])

    firstSum = secondSum = 0

    while numberFirst > 0 or numberSecond > 0:

        firstSum += numberFirst % 2
        secondSum += numberSecond % 2

        numberFirst //= 10
        numberSecond //= 10

    if firstSum == secondSum:
        
        message = 'YES'
    else:
        message = 'NO'
else:
    message = 'Ошибка! Введите 6 значное число'


print(message)



