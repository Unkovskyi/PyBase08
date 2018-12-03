# Task 2_3

# 1 способ
factorial = 0
natural = int(input('input natural number: '))

while natural < 0:
    natural = print('You input not natural number')
    natural = int(input('input natural number: '))

else:
    if natural >= 0:
        factorial = 1
    for i in range(2, natural + 1):
        factorial *= i
print('factorial {} is {}'.format(natural, factorial))

# 2 способ
import math  # импорт библиотеки math для задействования функции factorial

natural = int(input('input natural number: '))
if natural < 0:
    print('You input not natural number')
result = math.factorial(natural)
print('factorial {} is {}'.format(natural, result))