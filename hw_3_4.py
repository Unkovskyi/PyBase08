# Task_4_1

import string
from string import whitespace, punctuation

print('whitespace = {}'.format(repr(whitespace)))
print('punctuation = {}'.format(repr(punctuation)))
print('---------------------------------------------')


def print_table_1(inp_dict):
    res = ' '
    out_keys = inp_dict.keys()
    for i in out_keys:
        res = i + ' -  ' + str(inp_dict[i])
        print(res)


def del_punctuation(inp_text):  # функция удаления знаков пунктуации
    for i in string.punctuation:
        if i != "'":
            inp_text = inp_text.replace(i, ' ')
        else:
            continue
    return inp_text


def get_vocabulary(text):
    result = {}
    text = text.lower().split()
    for i in text:
        if i in result:
            continue
        else:

            Flaf = False
            while Flaf == False:
                key = input('input translate of new word  <<{}>>: '.format(i))
                if key in string.punctuation or key == ' ':
                    print('  !!!  invalid input please repeat')

                else:
                    result.update({i: key})
                    Flaf = True
    return result


start_inp = False
inp_ = ''
while start_inp == False:
    inp = input('Input text: ')

    if inp not in string.whitespace:
        inp_ = inp_ + ' ' + inp.replace('\n', ' ')
    else:
        inp_ = del_punctuation(inp_)
        inp_ = get_vocabulary(inp_)
        print('---------------- \nVocabulary\n----------------')
        inp = print_table_1(inp_)
        start_inp = True

