# Task_3_2

import string
from string import whitespace, punctuation

print('whitespace = {}'.format(repr(whitespace)))
print('punctuation = {}'.format(repr(punctuation)))
print('---------------------------------------------')


def del_punctuation(inp_text):  # функция удаления знаков пунктуации
    for i in string.punctuation:
        if i != "'":
            inp_text = inp_text.replace(i, "")
        else:
            continue
    return inp_text


start_inp = False
inp_ = ''
while start_inp == False:
    inp = input('Input text: ')
    if inp not in string.whitespace:
        inp_ = inp_ + ' ' + inp.replace('\n', '')

    else:
        inp_ = del_punctuation(inp_)
        inp_ = sorted(inp_.lower().split())
        print(inp_)
        start_inp = True