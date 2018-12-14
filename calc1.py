# функции которые используются в програме

import string
from string import whitespace, punctuation


def add(a, b):
    """add - функция которая находит сумму двух чисел"""
    return a + b


def sub(a, b):
    """sub - функция которая находит разницу двух чисел"""
    return a - b


def mul(a, b):
    """mul-функция которая умножает одно число на другое"""
    return a * b


def div(a, b):
    """div-функция которая делит одно число на другое"""
    flag = True
    res = None
    try:
        res = a / b
        flag = False
    except(ZeroDivisionError) as e:
        print('!!! Error2:', e)
        print('Try again')
    return res


# начало програмы

Flaf = False
while Flaf == False:
    name = input('input yor name: ')
    if name in string.punctuation or name == ' ':
        print('  !!!  invalid input please repeat')
    else:
        Flaf = True
print('Hello, ', name)

start = 'y'
list_of_oper = {'+': add, '-': sub, '*': mul, '/': div}
while start == 'y':
    start = input('Do you want to calculate?    [y]-yes, [any  button]-no:  ')
    if start == 'y':
        flag = True
        while flag:
            try:
                number_1 = float(input('input number 1:  '))
                number_2 = float(input('input number 2:  '))
                oper = input('input operation from the list {}: '.format(list(list_of_oper.keys()))).strip()
                flag = False
            except(ValueError) as e:
                print('!!! Error1:', e)
                print('Try again')

            res = None
        if oper in list(list_of_oper.keys()):
            res = list_of_oper[oper](number_1, number_2)
            print('Result:  {} {} {}={}'.format(number_1, oper, number_2, res))
        else:
            print('sorry, this operation is not in the list, try again ')
print('Ok, byе')