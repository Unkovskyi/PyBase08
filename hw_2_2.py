# Tack 2_2
summa = 0
number_1 = int(float(input('input number 1: ')))  # ввод преобразовываем в целые числа
number_2 = int(float(input('input number 2: ')))  # ввод преобразовываем в целые числа

if number_1 > number_2:  # меняем местами переменные если 1- число больше 2-го
    number_1 = number_1 - number_2
    number_2 = number_2 + number_1
    number_1 = number_2 - number_1

for i in range(number_1, number_2 + 1):
    print(i)
    if i > 0:  # сумируем только натуральные числа: целые, больше нуля
        summa += i
print('-------------------')
print('The sum of all  natural number in the range from {} to {} is {}'.format(number_1, number_2, summa))