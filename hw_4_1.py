import string
from string import ascii_letters


def clear_word(word, filterstr):  # функция по очистке слова от заданных символов
    all_s = string.punctuation + string.whitespace + string.digits + string.ascii_letters
    result = word
    for i in range(len(word)):
        if word[i] in filterstr:
            result = result.replace(word[i], '')
        elif word[i] not in all_s:
            raise ValueError('the text contains non-english characters: symbol {}:position {}'.format(word[i], i))
    return result


filt = list(input('input filter symbol: '))  # демонстрация работы функции
word = input('input text: ')

try:
    res = clear_word(word, filt)
    print(res)
except ValueError as e:
    print(e)