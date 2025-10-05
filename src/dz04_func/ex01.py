"""1. Задан текст случайным образом.

import random
import string
n = 1000
n_word = 10
actions = ('upper', 'reverse', 'double', 'del_digits', 'del_even', 'replace')
text = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])
Напишите функцию, которая в качестве аргументов получает:
text – исходный текст
n_word – количество слов
actions – кортеж действий.
Функция разбивает пробелами текст на необходимое количество слов различной длины
(используйте random) и к каждому получившемуся слову применяет полученные действия. К
первому слову – первое действие, ко второму слову – второе действие и т.д., к седьмому
слову – первое действие.
Действия простые:
'upper' - сделать все буквы заглавными
'reverse' - слово в обратном порядке
'double' - продублировать слово (станет слово + это же слово)
'del_digits' - удалить из слова цифры
'del_even' - удалить каждый чётный символ
'replace' - заменить каждую цифру слова на “Python”
Необязательно, но приветствуется при выполнении задания использование map(), reduce() и
т.д., а также lambda-функций.
"""

from functools import reduce
import random
import string

#from functools import reduce

def pysplit(letter):
        """Qweqwe."""
        if letter.isdigit():
            return 'Python'
        else:
            return letter

def split_actions(text: str, n_word:int, actions:tuple)->list:
    """Sasdfasf."""
    points_list = random.sample(range(1,len(text)),n_word-1)
    points_list.append(0)
    points_list.append(len(text))    
    points_list.sort()

    words_list     = []
    words_list_mod = []
    for i in range(n_word):
        subtext = text[points_list[i]:points_list[i+1]]
        words_list.append(subtext)

        j = i if len(actions) > i else i % len(actions) 

        subtext_new = str()
        match actions[j]:
            case 'upper': 
                subtext_new = subtext.upper()
            case 'reverse':
                subtext_new = subtext[::-1]
            case 'double':
                subtext_new = subtext * 2 
            case 'del_digits':
                subtext_new = ''.join(filter(lambda x: x.isalpha() , subtext))
            case 'del_even':
                subtext_new = subtext[::2]
            case 'replace':
                subtext_new = ''.join(map(pysplit, subtext))

        words_list_mod.append(subtext_new)

        print(f'{subtext} ---№{i+1} исходное')
        print(f'{subtext_new} ---№{i+1} модифицированное {actions[j]}')    
    


    return words_list, words_list_mod


n = 1000
n_word = 10
actions = ('upper', 'reverse', 'double', 'del_digits', 'del_even', 'replace')

text = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])

words_list, words_list_mod = split_actions(text, n_word, actions)

print(f'{len(text)} - длина текста') 
print(f'{len(reduce(lambda x1, x2: x1 + x2, words_list))} - сумма длин слов')

