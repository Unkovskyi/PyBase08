# Task_3_5

import string
from string import whitespace, punctuation

print('whitespace = {}'.format(repr(whitespace)))
print('punctuation = {}'.format(repr(punctuation)))
print('---------------------------------------------')


def print_table_1(inp_dict):  # функция для "красивого" вывода словаря
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


def get_vocabulary(text):  # функция для формирования словаря
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


def translate(text, dictionary):  # функция для перевода введенного текста
    result = ''
    text = del_punctuation(text).lower().split()
    for i in text:
        result = result + ' ' + dictionary[i]
    return result


start_inp = False
inp_ = ''
out_inp = ''

while start_inp == False:
    inp = input('Input text: ')

    if inp not in string.whitespace:
        inp_ = inp_ + ' ' + inp.replace('\n', ' ')  # для словаря
        out_inp = out_inp + ' ' + inp.replace('\n', ' ')  # для перевода введенного текста
    else:
        inp_ = del_punctuation(inp_)
        inp_ = get_vocabulary(inp_)
        print('---------------- \nVocabulary\n----------------')
        print_table_1(inp_)
        print('---------------- \nTranslation\n----------------')
        print('translation is: {}'.format(translate(out_inp, inp_)))
        start_inp = True