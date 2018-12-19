import string
from string import whitespace, punctuation, digits, ascii_letters, ascii_lowercase, ascii_uppercase


def clear_word(word, filterstr):  # функция по очистке слова от заданных символов
    all_s = string.punctuation + string.whitespace + string.digits + string.ascii_letters
    result = word
    for i in range(len(word)):
        if word[i] in filterstr:
            result = result.replace(word[i], '')
        elif word[i] not in all_s:
            raise ValueError(word[i], i)
    return result


def del_punctuation(inp_text):  # функция удаления знаков пунктуации
    s = string.whitespace + string.punctuation + string.digits
    for i in s:
        if i != "'":
            inp_text = inp_text.replace(i, ' ')
        else:
            continue
    return inp_text


rus_uppercase = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦШЩЪЫЬЭЮЯ'
rus_lowercase = rus_uppercase.lower()
rus_alf = rus_uppercase + rus_lowercase  # руский алфавит


def get_eng_words(
        text):  # Функция которая возвращает список слов из текста, которые состоят исключительно из символов английского алфавита.
    text = clear_word(del_punctuation(text), rus_alf)
    clear_text = set(text.lower().split())
    result = []
    for i in clear_text:
        if i in clear_text:
            result.append(i.lower())

    return result


word = input('input text: ')  # для демонстрации функции
result = get_eng_words(word)
print(result)