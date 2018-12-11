# Task_3_1

import string
from string import whitespace, punctuation

print('whitespace = {}'.format(repr(whitespace)))
print('punctuation = {}'.format(repr(punctuation)))
print('---------------------------------------------')


def dict_(inp):  # функция которая считает слова в веденной строке
    inp = inp.lower().split()
    dict_ = dict()
    for i in inp:
        if i in dict_:
            dict_[i] = dict_[i] + 1
        else:
            dict_[i] = 1
    return dict_


def del_punctuation(inp_text):  # функция удаления знаков пунктуации
    for i in string.punctuation:
        if i != "'":
            inp_text = inp_text.replace(i, "")
        else:
            continue
    return inp_text


def leng_max(inp_list):  # функция для подсчета максимальной длинны слова из списка
    inp_list = inp_list.lower().split()
    leng = []
    for i in inp_list:
        leng_i = len(i)
        leng.append(leng_i)
        max_len = max(leng)
    return max_len


def print_table(inp_dict):
    res = ' '
    outp = dict_(inp_dict)
    out_keys = outp.keys()
    for i in out_keys:
        res = '|' + i + (' ' * (leng_max(inp_dict) - len(i))) + '|' + str(outp[i]) + '|'
        print(res)


start_inp = False
inp_ = ''
while start_inp == False:
    inp = input('Input text: ')

    if inp not in string.whitespace:
        inp_ = inp_ + ' ' + inp.replace('\n', '')
    else:
        inp_ = del_punctuation(inp_)
        inp_ = print_table(inp_)
        start_inp = True

