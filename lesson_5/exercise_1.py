# -*- coding: utf-8 -*-

# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
with open('exercise_1.txt', 'w') as my_file:
    while True:
        file_input = input()
        if len(file_input) > 0:
            my_file.write(file_input + '\n')
        else:
            break