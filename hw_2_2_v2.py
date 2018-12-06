# Tack 2_2_upd

import math  # импорт библиотеки math для использования функций ceil и floor

summa = 0
number_1 = float(input('input number 1: '))
number_2 = float(input('input number 2: '))

if number_1 > number_2:  # меняем местами переменные если 1- число больше 2-го
    number_1 = number_1 - number_2
    number_2 = number_2 + number_1
    number_1 = number_2 - number_1

number_1 = math.ceil(number_1)  # функция ceil округление до верхнего целого чисоа
number_2 = math.floor(number_2)  # функция floor округление до нижнего целого чисоа

for i in range(number_1, number_2 + 1):
    print(i)
    if i > 0:  # сумируем только натуральные числа: целые, больше нуля
        summa += i
print('-------------------')
print('The sum of all  natural number in the range from {} to {} is {}'.format(number_1, number_2, summa))