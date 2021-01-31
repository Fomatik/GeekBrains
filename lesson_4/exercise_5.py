# -*- coding: utf-8 -*-

# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce


# my_list_1 = reduce(lambda a, x: a * x, range(100, 1001, 2))
# print(my_list_1)


def my_func(a, x):
    return a * x


list_num = [el for el in range(100, 1001) if el % 2 == 0]
print(f'Список чётных чисел от 100 до 1000: {list_num}')
print(f'Произведение всех элементов списка: {reduce(my_func, list_num)}')

