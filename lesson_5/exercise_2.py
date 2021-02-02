# -*- coding: utf-8 -*-

# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
with open('exercise_2.txt', 'r') as my_file:
    line = my_file.readlines()
    print(f'Количество строк: {len(line)}')
    n = 1
    for i in line:
        word = len(i.split())
        print(f'Количество слов в строке {n}: {word}')
        n += 1
