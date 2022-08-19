"""
Для массива целых чисел найдите непрерывный подмассив (содержащий хотя бы одно число),
который имеет наибольшую сумму, и верните его сумму.
"""

import sys
input = sys.stdin
input_set = list(map(int, input.readline().split()))

def max_sum(input_set):
    max_sum = 0
    sum = 0
    for i in input_set:
        sum += i
        if sum > max_sum:
            max_sum = sum
        elif sum < 0:
            sum = 0
    return max_sum

max_sum = max_sum(input_set)
print(max_sum)
