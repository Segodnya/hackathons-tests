"""
На вход подается натуральное число n (0 < n <= 1000).
Вернуть строковое значение 'true', если число простое, иначе вернуть 'false'.
Простое число - это натуральное число,
единственными делителями которого являются только оно само и единица.
(1 - не является простым числом)
"""

import sys
input = sys.stdin
number = int(input.readline().split()[0])

def check_prime(number):
    if number == 1:
        return 'false'
    for i in range(2, number):
        if number % i == 0:
            return 'false'
    return 'true'


result = check_prime(number)
print(result)