"""
Дано целое положительное число.
Вернуть сумму всех цифр этого числа.
"""

import sys
input = sys.stdin
string = input.readline().split()[0]
print(sum(map(int, string)))