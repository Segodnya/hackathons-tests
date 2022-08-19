"""
Дано 2 строки, переданные через пробел.
Вернуть строковое значение 'true', если строки являются анаграммами,
иначе вернуть 'false'.

Анаграмма – это слово или фраза, образованная путем перестановки букв
другого слова или фразы, с использованием всех исходных букв ровно один раз.
"""

import sys
input = sys.stdin
string1, string2 = input.readline().split()

def check_anagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    string1 = list(string1)
    string2 = list(string2)
    string1.sort()
    string2.sort()
    if string1 == string2:
        return 'true'
    else:
        return 'false'

result = check_anagram(string1, string2)
print(result)